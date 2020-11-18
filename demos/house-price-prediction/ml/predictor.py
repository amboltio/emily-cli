from ml.model import Model
import numpy as np

class Predictor:
    """
    The Predictor class is used for making predictions using a trained model instance based on the Model class
    defined in ml.model.py and the training steps defined in ml.trainer.py
    """

    def __init__(self):
        self.model_path = ""
        self.model = None

    def predict(self, sample, model_path):
        # Loads a trained instance of the Model class
        # If no model has been trained yet proceed to follow the steps in ml.trainer.py
        self.model = Model()
        self.model = self.model.load_model(model_path)
        self.model_path = model_path

        # Preprocess the inputted sample to prepare it for the model
        preprocessed_sample = self._preprocess(sample)

        # Forward the preprocessed sample into the model as defined in the __call__ function in the Model class
        prediction = self.model(preprocessed_sample)

        # Postprocess the prediction to prepare it for the client
        prediction = self._postprocess(prediction)

        return prediction

    def _preprocess(self, sample):
        return np.array(float(sample)).reshape(-1, 1)

    def _postprocess(self, prediction):
        return "$" + str((float(prediction) * 1000))

    def __call__(self, sample, model_path):
        return self.predict(sample, model_path)

