
from ml.model import Model


class Trainer:
    """
    The Trainer class is used for training a model instance based on the Model class found in model.model.py.
    In order to get started with training a model the following steps needs to be taken:
    1. Define the Model class in model.model.py
    2. Prepare train data on which the model should be trained with by implementing the _read_train_data() function and
    the _preprocess_train_data() function
    """

    def __init__(self):
        self.model = Model()  # creates an instance of the Model class (see guidelines in model.model.py)

    def train(self, dataset_path, save_path):
        """
        Starts the training of a model based on data loaded by the self._load_train_data function
        """
        # Read the dataset from the dataset_path
        train_data = self._load_train_data(dataset_path)

        # Preprocess the dataset
        preprocessed_train_data = self._preprocess_train_data(train_data)

        # TODO 3: implement steps which trains a model using the preprocessed_train_data
        # e.g. model.fit() for sklearn models

        # Save the trained model
        return self.model.save_model(save_path)

    def _load_train_data(self, dataset_path):
        """
        TODO 1: Implement steps for reading the dataset used for training
        e.g. Reading data from a mounted drive 'data/train/' (pandas.read_csv()) or from a database
        """
        train_dataset = None
        return train_dataset

    def _preprocess_train_data(self, train_data):
        """
        TODO 2.: Implement preprocessing steps which prepares the dataset for training
        e.g. normalizing the data, removing noisy data, splitting up the data into input values and target values
        """
        preprocessed_train_data = train_data
        return preprocessed_train_data

    def __call__(self, dataset_path, save_path):
        return self.train(dataset_path, save_path)

