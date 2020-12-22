
from ml.model import Model

import random
import json
import pickle
import os

# Natural language toolkit (used for semming and tokenization)
import nltk
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
from nltk.stem.snowball import DanishStemmer

# PyTorch used for deep learning
import torch
from torch.optim import SGD
from torch.nn import CrossEntropyLoss
from torch.utils.data import TensorDataset, DataLoader


class Trainer:

    def __init__(self):
        self.ds = DanishStemmer()
        self.model = Model()

    def train(self, request, batch_size=4, epochs=200):
        """Fits the model to the specified dataset and saves it

        Parameters:
        dataset_path (str): The path to the dataset used for training
        batch_size (int): The batch size during training (default=4)
        epochs (int): The number of epochs to train for (default=200)
        model_dir (str): The location for the model to be saved
                         (default=None, will create a folder by datetime)

        Returns:
        True - given that nothing fails
        """

        dataset_path = request.args['dataset_path']
        save_path = request.args['save_path']

        self.batch_size = batch_size
        self.epochs = epochs

        # create the model save directory if it does not already exist
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Read the dataset from the dataset_path
        train_data = self._load_train_data(dataset_path)

        # Preprocess the dataset
        data_loader, input_size, output_size = self._preprocess_train_data(train_data, save_path)

        # Define network
        self.model.define_network_layers(input_size, output_size)

        # Compile model. Stochastic gradient descent with Nesterov accelerated gradient
        self.model.train()
        optimizer = SGD(self.model.parameters(), lr=0.01, weight_decay=1e-5, momentum=0.9, nesterov=True)
        criterion = CrossEntropyLoss()

        loss_history = []
        acc_history = []

        # Fitting and saving the model
        for epoch in range(epochs):
            epoch_loss = 0
            epoch_acc = 0
            for batch in data_loader:
                inputs, labels = batch
                # zero the paramter gradients
                # to prevent graidnet accumulation
                optimizer.zero_grad()

                # perform forward pass
                outputs = self.model(inputs)

                # cross entropy loss expectes the target as a single
                # number between 0 and #classses which is determined as:
                target = torch.max(labels, 1)[1]

                # calculate loss
                loss = criterion(outputs, target)

                # determine paramter gradients
                loss.backward()

                # update paramters based on gradients
                optimizer.step()

                # calculte accuracy
                # this accuracy is simply the percentage of predictions
                # with the correct class having the highest activation
                pred_idxs = torch.argmax(outputs, dim=1)
                label_idxs = torch.argmax(labels, dim=1)
                acc = (pred_idxs == label_idxs).float().sum() / len(inputs)

                # accumulate loss and acc for the epoch
                epoch_loss += loss
                epoch_acc += acc

            # calculate epoch loss and acc and append it to the training history
            epoch_loss = epoch_loss / len(data_loader)
            epoch_acc = epoch_acc / len(data_loader)
            loss_history.append(epoch_loss)
            acc_history.append(epoch_acc)

        # Define meta data used to save as 'checkpoint'
        meta_data = {'epoch': epoch + 1,
                     'loss': float(epoch_loss),
                     'acc': float(epoch_acc),
                     'input_size': input_size,
                     'output_size': output_size,
                     'optimizer': str(optimizer).splitlines(),
                     'model': str(self.model).splitlines()}

        # Save training diagram
        self.model.save_training_diagram(save_path, acc_history, loss_history)

        # Save and return the trained model
        return self.model.save_model(save_path, meta_data, optimizer)

    def _load_train_data(self, dataset_path):
        # open data file
        data_file = open(dataset_path, encoding='utf-8').read()
        # load it as a dictionary from the json file
        train_dataset = json.loads(data_file)
        return train_dataset

    def _preprocess_train_data(self, train_data, save_path):
        # determine the classes, documents a.k.a. patterns and the vocabulary of the dataset
        classes, documents, vocab = self._define_vocab_classes_documents(train_data, save_path)
        # create a dataloader and determine needed network input and output size
        dataloader, input_size, output_size = self._create_dataloader(classes, documents, vocab)
        return dataloader, input_size, output_size

    def _define_vocab_classes_documents(self, train_data, save_path):
        intents = train_data
        vocab = []
        classes = []
        documents = []
        ignore_words = ['?', '!']

        for intent in intents['intents']:
            for pattern in intent['patterns']:
                # take each word and tokenize it
                w = nltk.word_tokenize(pattern, language='danish')
                vocab.extend(w)
                # adding documents
                documents.append((w, intent['tag']))
                # adding classes to the class list
                if intent['tag'] not in classes:
                    classes.append(intent['tag'])

        # filter words to ignore
        vocab = [self.ds.stem(w) for w in vocab if w not in ignore_words]

        # determine the set of unique words and classes
        vocab = sorted(list(set(vocab)))
        classes = sorted(list(set(classes)))

        # store vocabulary and class names
        pickle.dump(vocab, open(os.path.join(save_path, 'vocab.pkl'), 'wb'))
        pickle.dump(classes, open(os.path.join(save_path, 'classes.pkl'), 'wb'))

        return classes, documents, vocab

    def _create_dataloader(self, classes, documents, vocab):
        inputs = []
        labels = []
        output_empty = [0] * len(classes)
        for doc in documents:
            # initializing bag of words
            bag = []
            # list of tokenized words for the pattern
            pattern_words = doc[0]
            # lemmatize each word - create base word, in attempt to represent related words
            pattern_words = [self.ds.stem(word) for word in pattern_words]
            # create our bag of words array with 1, if word match found in current pattern
            for w in vocab:
                bag.append(1) if w in pattern_words else bag.append(0)

            # output is a '0' for each tag and '1' for current tag (for each pattern)
            output_row = list(output_empty)
            output_row[classes.index(doc[1])] = 1

            inputs.append(bag)
            labels.append(output_row)

        # shuffle features
        data = list(zip(inputs, labels))
        random.shuffle(data)
        inputs, labels = zip(*data)

        # convert to PyTorch tensor of appropriate type
        inputs = torch.Tensor(inputs)
        labels = torch.Tensor(labels)

        # determine output and input size
        input_size = len(inputs[0])
        output_size = len(labels[0])

        # create data generator
        training_set = TensorDataset(inputs, labels)
        return DataLoader(training_set, self.batch_size), input_size, output_size

    def __call__(self, request):
        return self.train(request)

