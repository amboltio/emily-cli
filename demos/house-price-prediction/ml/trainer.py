
from ml.model import Model
import pandas as pd


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
        dataset_path = request.dataset_path
        save_path = request.save_path

        # Read the dataset from the dataset_path
        train_data = self._load_train_data(dataset_path)

        # Preprocess the dataset
        preprocessed_train_data = self._preprocess_train_data(train_data)

        # Train the model
        X = pd.DataFrame(preprocessed_train_data[[
                         'sqft_living', 'condition', 'zipcode']])
        y = pd.DataFrame(preprocessed_train_data['price'])
        self.model.fit(X, y)

        # Save the trained model
        return self.model.save_model(save_path)

    def _load_train_data(self, dataset_path):
        train_dataset = pd.read_csv(dataset_path)
        return train_dataset

    def _preprocess_train_data(self, train_data):
        preprocessed_train_data = train_data.dropna()
        return preprocessed_train_data

    def __call__(self, request):
        return self.train(request)
