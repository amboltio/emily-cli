
from ml.model import Model

import pickle
import json
import os

# Natural language toolkit (used for semming and tokenization)
import nltk
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
from nltk.stem.snowball import DanishStemmer

# PyTorch used for deep learning
import torch
from torch.nn import CrossEntropyLoss
from torch.utils.data import TensorDataset, DataLoader


class Evaluator:

    def __init__(self):
        # Disabling gradient calculation to reduce memory consumption for computations
        torch.no_grad()

        self.model_path = ""

        # initialize stemmer
        self.ds = DanishStemmer()

    def evaluate(self, request, batch_size=4, load_method='state dict'):
        """
        Evaluates a trained model located at 'model_path' based on test data from the self._load_test_data function

        Parameters:
        dataset_path (str): The path to the dataset used for evaluation
        model_path (str): The path to the model to be evaluated
        batch_size (int): The batch size during evaluation (default=4)
        load_method (str): Model loading method can be 'state dict' or 'checkpoint' (default='state dict')

        Returns:
        evaluation result dict {'loss': float, 'acc': float}: loss and accuracy
        """

        dataset_path = request.args['dataset_path']
        model_path = request.args['model_path']

        # (Re)load model if the given model path differes from the privous model path
        if model_path != self.model_path:
            self.model = Model()
            self.model.load_model(model_path, load_method)
            self.model.eval()

            # load configuration data
            self.vocab = pickle.load(open(os.path.join(model_path, 'vocab.pkl'), 'rb'))
            self.classes = pickle.load(open(os.path.join(model_path, 'classes.pkl'), 'rb'))

            self.model_path = model_path

        self.batch_size = batch_size

        # Read the dataset from the dataset_path
        test_data = self._load_test_data(dataset_path)

        # Preprocess dataset to prepare it for the evaluator
        data_loader = self._preprocess_test_data(test_data)

        # Fitting and saving the model
        criterion = CrossEntropyLoss()
        loss = 0
        acc = 0
        for batch in data_loader:
            inputs, labels = batch

            # perform forward pass
            outputs = self.model(inputs)

            # cross entropy loss expectes the target as a single
            # number between 0 and #classses which is determined as:
            target = torch.max(labels, 1)[1]

            # calculate loss
            loss += criterion(outputs, target)

            # calculte accuracy
            # this accuracy is simply the percentage of predictions
            # with the correct class having the highest activation
            pred_idxs = torch.argmax(outputs, dim=1)
            label_idxs = torch.argmax(labels, dim=1)
            acc += (pred_idxs == label_idxs).float().sum() / len(inputs)

        loss = loss / len(data_loader)
        acc = acc / len(data_loader)

        return {"loss": float(loss), "acc": float(acc)}

    def _load_test_data(self, dataset_path):
        # open data file
        data_file = open(dataset_path, encoding='utf-8').read()
        # load it as a dictionary from the json file
        test_dataset = json.loads(data_file)
        return test_dataset

    def _preprocess_test_data(self, test_data):
        # determine the documents a.k.a. patterns in the dataset
        documents = self._define_documents(test_data)
        # create a dataloader
        dataloader = self._create_dataloader(documents)
        return dataloader

    def _define_documents(self, test_data):
        intents = test_data
        documents = []

        for intent in intents['intents']:
            for pattern in intent['patterns']:
                # take each word and tokenize it
                w = nltk.word_tokenize(pattern, language='danish')
                # adding documents
                documents.append((w, intent['tag']))

        return documents

    def _create_dataloader(self, documents):
        inputs = []
        labels = []
        output_empty = [0] * len(self.classes)
        for doc in documents:
            # initializing bag of words
            bag = []
            # list of tokenized words for the pattern
            pattern_words = doc[0]
            # lemmatize each word - create base word, in attempt to represent related words
            pattern_words = [self.ds.stem(word) for word in pattern_words]
            # create our bag of words array with 1, if word match found in current pattern
            for w in self.vocab:
                bag.append(1) if w in pattern_words else bag.append(0)

            # output is a '0' for each tag and '1' for current tag (for each pattern)
            output_row = list(output_empty)
            output_row[self.classes.index(doc[1])] = 1

            inputs.append(bag)
            labels.append(output_row)

        # convert to PyTorch tensor of appropriate type
        inputs = torch.Tensor(inputs)
        labels = torch.Tensor(labels)

        # create data generator
        test_set = TensorDataset(inputs, labels)

        return DataLoader(test_set, self.batch_size)

    def __call__(self, request):
        return self.evaluate(request)

