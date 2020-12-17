
from ml.predictor import Predictor
from ml.trainer import Trainer
from ml.evaluator import Evaluator

class Emily:
    """
    The Emily class is simply a wrapper class which creates instances of:
    - The Predictor class (see ml.predictor.py)  # Used for making predictions with a trained model
    - The Trainer class (see ml.trainer.py)      # Used for training a model
    - The Evaluator class (see ml.evaluator.py)  # Used for evaluating a trained model

    """

    def __init__(self):
        self.predictor = Predictor()    # Creates instance of the Predictor class
        self.trainer = Trainer()        # Creates instance of the Trainer class
        self.evaluator = Evaluator()    # Creates instance of the Evaluator class

    def predict(self, request):
        """
        This function calls the __call__ function from the Predictor class in ml.predictor.py.
        Make sure the __call__ method is implemented correctly
        """
        return self.predictor(request)
    
    def train(self, request):
        """
        This function calls the __call__ function from the Trainer class in ml.trainer.py.
        Make sure the __call__ method is implemented correctly
        """
        return self.trainer(request)

    def evaluate(self, request):
        """
        This function calls the __call__ function from the Evaluator class in ml.evaluator.py.
        Make sure the __call__ method is implemented correctly
        """
        return self.evaluator(request)

