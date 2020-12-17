
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

    def evaluate(self, request):
        """
        Evaluates a trained model located at 'model_path' based on test data from the self._load_test_data function
        """

        # Unpack request
        dataset_path = request.args['dataset_path']
        model_path = request.args['model_path']

        # Loads a trained instance of the Model class
        # If no model has been trained yet proceed to follow the steps in ml.trainer.py
        self.model = Model()
        self.model = self.model.load_model(model_path)
        self.model_path = model_path

        # Read the dataset from the dataset_path
        test_data = self._load_test_data(dataset_path)

        # Preprocess dataset to prepare it for the evaluator
        test_dataset = self._preprocess_test_data(test_data)

        # Evaluate model
        predictions = self.model(test_dataset['RM'].values.reshape(-1, 1))
        actual = test_dataset['MEDV']

        score = mean_absolute_error(actual, predictions)

        return score

    def _load_test_data(self, dataset_path):
        test_dataset = pd.read_csv(dataset_path)
        return test_dataset

    def _preprocess_test_data(self, test_data):
        preprocessed_test_data = test_data.dropna()
        return preprocessed_test_data

    def __call__(self, request):
        return self.evaluate(request)
