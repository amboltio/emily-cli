
import torch

from ml.transforms import test_transforms


class Predictor:
    """
    The Predictor class is used for making predictions using a trained model instance based on the Model class
    defined in ml.model.py and the training steps defined in ml.trainer.py
    """

    def __init__(self, model):
        self.model = model
        self.transforms = test_transforms()

        use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if use_cuda else "cpu")

    def predict(self, img):
        """
        Performs prediction on a sample using the model at the given path
        """
        # Transform image into a tensor with appropriate dimensions
        self.model.eval()
        image = self.transforms(img)
        image = image.unsqueeze(0)
        image = image.to(self.device)

        # Input the image into ResNet to extract features and then into the classifier model
        resnet_features = self.resnet(image)
        prediction = self.model(resnet_features)

        prediction_confidence = self.postprocess(prediction)
        return prediction_confidence


    def postprocess(self, prediction):
        """
        Implement postprocessing steps which prepares the prediction for the client
        e.g. removing unnecessary decimal numbers from the prediction, transforming/formatting the prediction etc.
        Remove or ignore this function if no postprocessing steps are necessary
        """
        # Apply softmax to convert prediction values to probabilities
        prediction_confidence = torch.nn.functional.softmax(prediction, dim=1)

        # Convert tensor to numpy array
        prediction_confidence = prediction_confidence.detach().cpu().numpy()[0]

        prediction_confidence = round(prediction_confidence[1] * 100, 2)

        return prediction_confidence



