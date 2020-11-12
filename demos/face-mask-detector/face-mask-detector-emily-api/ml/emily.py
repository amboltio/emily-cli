
from ml.predictor import Predictor
from ml.trainer import Trainer
from ml.evaluator import Evaluator


class Emily:
    """
    The Emily class is simply a wrapper class which creates instances of:
    - The Predictor class (see model.predictor.py)  # Used for making predictions with a trained model
    - The Trainer class (see model.trainer.py)      # Used for training a model
    - The Evaluator class (see model.evaluator.py)  # Used for evaluating a trained model

    Get started by following the steps in model.trainer.py and model.model.py
    """

    def __init__(self):
        self.predictor = Predictor()    # Creates instance of the Predictor class
        self.trainer = Trainer()        # Creates instance of the Trainer class
        self.evaluator = Evaluator()    # Creates instance of the Evaluator class

    def predict(self, sample, model_path):
        """
        This function calls the __call__ function from the Predictor class in model.predictor.py.
        Make sure the __call__ method is implemented correctly
        """
        return self.predictor(sample, model_path)

    def train(self, dataset_path, save_path):
        """
        This function calls the __call__ function from the Trainer class in model.trainer.py.
        Make sure the __call__ method is implemented correctly
        """
        return self.trainer(dataset_path, save_path)

    def evaluate(self, dataset_path, model_path):
        """
        This function calls the __call__ function from the Evaluator class in model.evaluator.py.
        Make sure the __call__ method is implemented correctly
        """
        return self.evaluator(dataset_path, model_path)

