
import torch

from src.data_utilities import create_data_loader
from src.transforms import test_transforms
from src.engine import calculate_accuracy
from src.model import Model
from src.requests import EvaluateRequest


class Evaluator:
    """
    The Evaluator class is used for evaluating a trained model instance.
    """

    def __init__(self, request: EvaluateRequest):

        # Set evaluation parameters
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.test_csv = request.test_csv
        self.batch_size = request.batch_size

        # initialize model object and load weights from a trained model instance
        self.model = Model()
        self.model.load_model(request.model_path)

        # Set the model's mode to evaluation (mean gradients will not be calculated which speeds up the process)
        torch.no_grad()
        self.model.eval()

    def evaluate(self):
        """
        Evaluates a trained model located at 'model_path' based on test data from the self._load_test_data function
        """

        # Create the pytorch dataLoader which takes care of feeding samples to the model
        test_data_loader = create_data_loader(
            csv_fp=self.test_csv,
            batch_size=self.batch_size,
            transform_fns=test_transforms(),
            shuffle=True
        )

        print(f'Evaluting model on data set from {self.test_csv}...')
        test_acc = 0.

        # Iterate over the test dataset
        for idx, batch in enumerate(self.test_data_loader):

            if (idx + 1) % 10 == 0:
                print(f'Processing batch {idx + 1}/{len(self.test_data_loader)}')

            data = batch['data'].to(self.device)
            labels = batch['label'].to(self.device)

            predictions = self.model(data)
            predicted_class = predictions.argmax(dim=1)

            test_acc += calculate_accuracy(predicted_class, labels)

        # Calculate accuracy for entire test dataset
        total_test_acc = None
        return total_test_acc

    def __call__(self):
        return self.evaluate()

