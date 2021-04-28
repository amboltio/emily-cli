
import torch
import base64

from PIL import Image
from io import BytesIO

from src.model import Model
from src.transforms import test_transforms


class Predictor:
    """
    The Predictor class is used for making predictions using a trained model instance based on the Model class
    defined in src.model.py and the training steps defined in src.trainer.py
    """

    def __init__(self, model_path):

        # Initialize model object
        self.model = Model()
        self.model.load_model(model_path)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # Disable gradient calculation and set model to eval mode
        torch.no_grad()
        self.model.eval()

        self.transform_fn = test_transforms()

    def predict(self, img_path):
        """
        Performs prediction on a data sample using the model at the given path
        """

        img = Image.open(img_path)

        # Transform the inputted sample to prepare it for the model
        data = self.transform_fn(img)
        # Returns a tensor with a dimension of size one at the specified position.
        data = data.unsqueeze(0)
        # Allocates the tensor to the cpu or gpu
        data = data.to(self.device)

        # Forward the preprocessed data sample into the model
        prediction = self.model(data)

        # Postprocess the prediction to prepare it for the client
        prediction_confidence = self.postprocess(prediction)

        return prediction_confidence

    def predict_webcam(self, img: str):
        """
        Performs prediction on a data sample using the model at the given path
        """
        # Convert the base64 encoded input image from the webcamera into a PIL Image
        img = Image.open(BytesIO(base64.b64decode(img)))
        img = img.convert('RGB')

        # Transform the inputted sample to prepare it for the model
        data = self.transform_fn(img)

        # Returns a tensor with a dimension of size one at the specified position.
        data = data.unsqueeze(0)

        # Allocates the tensor to the cpu or gpu
        data = data.to(self.device)

        # Forward the preprocessed data sample into the model
        prediction = self.model(data)

        # Postprocess the prediction to prepare it for the client
        prediction_confidence = self.postprocess(prediction)

        return prediction_confidence

    def postprocess(self, prediction):
        """
        postprocessing steps which prepares the prediction for the client
        e.g. rounding, converting the prediction etc. to prettify it.
        """

        # Apply softmax to convert prediction values to probabilities
        prediction_confidence = torch.nn.functional.softmax(prediction, dim=1)

        # Convert tensor to numpy array
        prediction_confidence = prediction_confidence.detach().cpu().numpy()[0]

        prediction_confidence = round(prediction_confidence[1] * 100, 2)

        return prediction_confidence

    def __call__(self, data):
        return self.predict(data)
