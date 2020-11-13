from ml.model import Model
import pandas as pd
from sklearn.metrics import mean_absolute_error

class Evaluator:
    """
    The Evaluator class is used for evaluating a trained model instance.
    In order to get started with evaluating a model the following steps needs to be taken:
    1. Train a model following the steps in ml.trainer.py
    2. Prepare test data on which the model should be evaluated on by implementing the _read_test_data() function and
    the _preprocess_test_data function
    """

    def __init__(self):
        self.model_path = ""
        self.model = None

    def evaluate(self, dataset_path, model_path):
        """
        Evaluates a trained model located at 'model_path' based on test data from the self._load_test_data function
        """
        # Loads a trained instance of the Model class
        # If no model has been trained yet proceed to follow the steps in ml.trainer.py
        self.model = Model()
        self.model = self.model.load_model(model_path)
        self.model_path = model_path

        # Read the dataset from the dataset_path
        test_data = self._load_test_data(dataset_path)

        # Preprocess dataset to prepare it for the evaluator
        test_dataset = self._preprocess_test_data(test_data)

        # TODO 3: implement steps which evaluates the model here
        # e.g. model.eval() for sklearn models
        predictions = self.model(test_dataset['RM'].values.reshape(-1, 1))
        actual = test_dataset['MEDV']

        score = mean_absolute_error(actual, predictions)

        return score

    def _load_test_data(self, dataset_path):
        """
        TODO 1: Implement steps for reading the dataset used for evaluation
        e.g. Reading data from a mounted drive 'data/test/' (pandas.read_csv()) or from a database
        """
        test_dataset = pd.read_csv(dataset_path)
        return test_dataset

    def _preprocess_test_data(self, test_data):
        """
        TODO 2.: Implement preprocessing steps which prepares the dataset for evaluation
        e.g. normalizing the data, removing noisy data, splitting up the data into input values and target values
        """
        preprocessed_test_data = test_data.dropna()
        return preprocessed_test_data

    def __call__(self, dataset_path, model_path):
        return self.evaluate(dataset_path, model_path)

