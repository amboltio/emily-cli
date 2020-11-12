
from ml.model import Model
from ml.face_detector import FaceDetector

import torch
import base64

import numpy as np

from torchvision import transforms
from PIL import Image
from io import BytesIO



class Predictor:
    """
    The Predictor class is used for making predictions using a trained model instance based on the Model class
    defined in ml.model.py
    """

    def __init__(self):
        self.model_path = ""
        self.model = None
        self.face_detector = FaceDetector()

    def predict(self, sample, model_path):
        # Loads a trained instance of the Model class
        # If no model has been trained yet proceed to follow the steps in model.trainer.py
        if model_path != self.model_path:
            self.model = Model()
            self.model.load_model(model_path)
            self.model_path = model_path
        else:
            self.model = self.model

        # Preprocess the inputted sample to prepare it for the model
        preprocessed_sample = self._preprocess(sample)

        # Forward the preprocessed sample into the model as defined in the __call__ function in the Model class
        if preprocessed_sample is None:
            prediction = None
            return prediction
            # Forward input into the model

        torch.no_grad()
        prediction = self.model(preprocessed_sample)

        # Postprocess the prediction to prepare it for the client
        prediction = self._postprocess(prediction)

        return prediction

    def _preprocess(self, sample):
        """
        Steps which prepares the inputted sample for the model
        """
        # Convert the base64 encoded input image into a PIL Image
        self._image = Image.open(BytesIO(base64.b64decode(sample)))
        self._image = np.asarray(self._image)
        self._image = self._image[:,:,:3]

        # Extract the face from the image
        self._face = self.face_detector.detect_face(self._image)
        if self._face is None:
            return None
        face, eyes = self._face
        (x1, y1, x2, y2) = face
        self._face_image = self._image[y1:y2, x1:x2].copy()
        self._face_image = Image.fromarray(self._image)

        # Define transformation functions and compose into a single PyTorch transformation function
        transform_fns = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor()
        ])

        # Transform image into a PyTorch Tensor
        tensor = transform_fns(self._face_image)

        # Append an extra dimension to the image (128, 128, 3) -> (1, 128, 128, 3)
        tensor = tensor.unsqueeze(0)

        # Prepare the sample for the CPU or GPU
        tensor = tensor.to(device="cpu")
        return tensor

    def _postprocess(self, prediction):
        """
        Steps which prepares the prediction for the client
        """
        _, prediction = prediction.max(1)
        prediction = prediction.detach().cpu().numpy()[0]
        return prediction

    def __call__(self, sample, model_path):
        return self.predict(sample, model_path)

