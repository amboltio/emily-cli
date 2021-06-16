
import torch

from src.model import Model
from src.transforms import test_transforms
from src.requests import PredictRequest

class Predictor:
    """
    The Predictor class is used for making predictions using a trained model instance based on the Model class
    defined in src.model.py and the training steps defined in src.trainer.py
    """

    def __init__(self, request: PredictRequest):

        # Initialize model object
        self.model = Model()
        self.model.load_model(request.model_path)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # Disable gradient calculation and set model to eval mode
        torch.no_grad()
        self.model.eval()

    def predict(self, data):
        """
        Performs prediction on a data sample using the model at the given path
        """

        # Transform the inputted sample to prepare it for the model
        data = test_transforms(data)    # Transforms the data into a pytorch tensor
        data = data.unsqueeze(0)        # Returns a tensor with a dimension of size one at the specified position.
        data = data.to(self.device)     # Allocates the tensor to the cpu or gpu

        # Forward the preprocessed data sample into the model
        prediction = self.model(data)

        # Postprocess the prediction to prepare it for the client
        prediction = self.postprocess(prediction)

        return prediction

    def postprocess(self, prediction):
        """
        postprocessing steps which prepares the prediction for the client
        e.g. rounding, converting the prediction etc. to prettify it.
        """
        return prediction

    def __call__(self, data):
        return self.predict(data)

