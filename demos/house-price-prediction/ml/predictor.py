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

    def predict(self, request):
        """
        Performs prediction on a sample using the model at the given path
        """

        # Unpack request
        sqft_living = request.sqft_living
        condition = request.condition
        zipcode = request.zipcode
        model_path = request.model_path

        # Loads a trained instance of the Model class
        # If no model has been trained yet proceed to follow the steps in ml.trainer.py
        self.model = Model()
        self.model = self.model.load_model(model_path)
        self.model_path = model_path

        # Preprocess the inputted sample to prepare it for the model
        preprocessed_sample = self._preprocess(sqft_living, condition, zipcode)

        # Forward the preprocessed sample into the model as defined in the __call__ function in the Model class
        prediction = self.model(preprocessed_sample)

        # Postprocess the prediction to prepare it for the client
        prediction = self._postprocess(prediction)

        return prediction

    def _preprocess(self, sqft_living, condition, zipcode):
        array = np.zeros((1, 3), dtype=int)
        array[0][0] = sqft_living
        array[0][1] = condition
        array[0][2] = zipcode
        return array

    def _postprocess(self, prediction):
        return "$" + str(prediction[0][0])

    def __call__(self, request):
        return self.predict(request)
