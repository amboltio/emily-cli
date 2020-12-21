
from ml.model import Model
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
import re
from tqdm import tqdm  # Wraps iterables and prints a progress bar
import os
import pickle

nltk.download('punkt')
nltk.download('stopwords')

stopwords = set(nltk.corpus.stopwords.words('english'))
porter = PorterStemmer()
clause_punctuation_regex = re.compile(r"^[.:;!?]$")
negating_word_regex = re.compile(r"(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|"
                                 r"couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't")


def _negate(words):
    negated = []
    is_negated = False

    for word in words:
        if clause_punctuation_regex.match(word):
            if is_negated:
                is_negated = False
            continue

        elif negating_word_regex.match(word):
            is_negated = True

        negated.append(f'{word}{"_NEG" if is_negated else ""}')
    return negated


def _normalize_words(words):
    normalized = []
    for word in words:
        if word in stopwords:
            continue
        normalized.append(porter.stem(word))

    return normalized


def normalize_text(text):
    # Optionally: explicitly handle negations, POS tags?
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = _negate(words)
    words = _normalize_words(words)
    return words


class Trainer:
    """
    The Trainer class is used for training a model instance based on the Model class found in ml.model.py.
    In order to get started with training a model the following steps needs to be taken:
    1. Define the Model class in ml.model.py
    2. Prepare train data on which the model should be trained with by implementing the _read_train_data() function and
    the _preprocess_train_data() function
    """

    def __init__(self):
        # creates an instance of the Model class (see guidelines in ml.model.py)
        self.model = Model()

    def train(self, request):
        """
        Starts the training of a model based on data loaded by the self._load_train_data function
        """

        # Unpack request
        dataset_path = './data/dataset.csv'
        save_path = './data/nb.pickle'

        # Read the dataset from the dataset_path
        train_data = self._load_train_data(dataset_path)

        # Preprocess the dataset
        preprocessed_train_data = self._preprocess_train_data(
            train_data, './data/preprocessed.pickle')

        # Fit the model
        self.model.fit(preprocessed_train_data)

        # Save the trained model
        self.model.save_model(save_path)

        return True

    def _load_train_data(self, dataset_path):
        with open(dataset_path) as fp:
            dataset = pd.read_csv(fp).values

        return dataset

    def _preprocess_train_data(self, train_data, preprocess_data_path):
        if preprocess_data_path and os.path.isfile(preprocess_data_path):
            with open(preprocess_data_path, 'rb') as fp:
                print(f'Loading {preprocess_data_path}...')
                return pickle.load(fp)

        preprocessed = []
        for review, sentiment in tqdm(train_data, '[Preprocessing training data...]'):
            preprocessed.append((normalize_text(review), sentiment))

        if preprocess_data_path:
            with open(preprocess_data_path, 'wb') as fp:
                print(f'Writing preprocessed data to {preprocess_data_path}')
                pickle.dump(preprocessed, fp)

        return preprocessed

    def __call__(self, request):
        return self.train(request)
