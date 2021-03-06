
from ml.model import Model

import numpy as np
import pickle
import os
import json
import random

# Natural language toolkit (used for semming and tokenization)
import nltk
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
from nltk.stem.snowball import DanishStemmer

# PyTorch used for deep learning
import torch
from torch.nn.functional import softmax


class Predictor:

    def __init__(self):
        # Disabling gradient calculation to reduce memory consumption for computations
        torch.no_grad()

        # Set inital model path to nothing
        self.model_path = ""

        # initialize stemmer
        self.ds = DanishStemmer()

        # load responses
        data_file = open('emily/data/responses_pizza_chatbot-danish.json',
                         encoding='utf-8').read()
        self.responses = json.loads(data_file)

    def predict(self, sample_item, load_method='state dict'):
        """
        Takes a sentence, converts its to a
        bag-of-words format and predicts its class/context

        Parameters:
        sample (str): The input sentence
        model_path (str): The path to the directory of the model
        load_method (str): Model loading method can be 'state dict' or 'checkpoint' (default='state dict')

        Returns:
        prediction dict {'class': str, 'prob': float}: class/context and probability
        OR
        (None): if no words from the sentence are contrained in the network vocabulary
        """

        sample = sample_item.sample
        model_path = sample_item.model_path

        # (Re)load model if the given model path differes from the privous model path
        if model_path != self.model_path:
            self.model = Model()
            self.model.load_model(model_path, load_method)
            self.model.eval()

            # load configuration data
            self.vocab = pickle.load(open(os.path.join(model_path, 'vocab.pkl'), 'rb'))
            self.classes = pickle.load(open(os.path.join(model_path, 'classes.pkl'), 'rb'))

            self.model_path = model_path

        # Preprocess the inputted sample to prepare it for the model
        preprocessed_sample = self._preprocess(sample)
        if preprocessed_sample is None:
            return None

        # Forward the preprocessed sample into the model as defined in the __call__ function in the Model class
        prediction = self.model(preprocessed_sample)
        if prediction is None:
            return None

        # Postprocess the prediction to prepare it for the client
        postprocessed_prediction = self._postprocess(prediction)
        return postprocessed_prediction


    def _preprocess(self, sample):
        # tokenize and stem the pattern
        sentence_words = nltk.word_tokenize(sample, language='danish')
        sentence_words = [self.ds.stem(word) for word in sentence_words]
        # convert to "bag of words" - matrix of N words, vocabulary matrix
        bow = [0] * len(self.vocab)
        for s in sentence_words:
            for i, w in enumerate(self.vocab):
                if w == s:
                    # assign 1 if current word is in the vocabulary position
                    bow[i] = 1
        bow = np.array(bow)
        # return None if the sum of bow is 0 size that means non of the words
        # in the input sentence is present in our vocabulary hence no valid
        # prediction can made. Otherwise return the bow in tensor form.
        if sum(bow) == 0:
            return None
        else:
            return torch.Tensor(bow)

    def _postprocess(self, prediction):
        # perform softmax to get class probabilies
        prediction = softmax(prediction, dim=0)

        # determine class with the highest probability
        class_prob, class_idx = torch.max(prediction, 0)

        # retrive the class name by index
        predicted_class = self.classes[class_idx.item()]

        out_response = 'Undskyld det forstod jeg ikke'
        if class_prob > 0.85:
            for response in list(self.responses['responses']):
                if response['tag'] == predicted_class:
                    out_response = random.choice(list(response['response_list']))

        return {"class": predicted_class, "prob": class_prob.item(), "response": out_response}

    def __call__(self, request):
        return self.predict(request)

