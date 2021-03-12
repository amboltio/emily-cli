import torch

from ml.model import Model
from ml.dataloader import CustomDataLoader
from ml.transforms import test_transforms


class Evaluator:
    """
    The Evaluator class is used for evaluating a trained model instance.
    In order to get started with evaluating a model the following steps needs to be taken:
    1. Train a model following the steps in ml.trainer.py
    2. Prepare test data on which the model should be evaluated on by implementing the _read_test_data() function and
    the _preprocess_test_data function
    """

    def __init__(self, model_path: str, test_csv: str, batch_size: int):
        # Check if GPU is available
        use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if use_cuda else "cpu")

        # init and load model
        self.model_path = model_path
        self.model = Model()
        self.model.load_model(self.model_path)

        # Set evulation parameters
        self.test_csv = test_csv
        self.batch_size = batch_size
        self.num_workers = 8

        # Instantiate pyTorch dataloaders
        self.test_data_loader = CustomDataLoader(
            self.test_csv, test_transforms(), self.batch_size, shuffle=True, num_workers=self.num_workers)

    def evaluate(self):
        """
        Evaluates a trained model located at 'self.model_path' based on test data from the self._load_test_data function
        """
        running_test_acc = 0.
        tps, fps, tns, fns = 0, 0, 0, 0
        # Set the model's mode to evaluation (mean gradients will not be calculated which speeds up the process)
        self.model.eval()

        print(f'Evaluting model on data set from {self.test_csv}...')
        for idx, (batched_sample) in enumerate(self.test_data_loader):
            print(f'Processing batch {idx + 1}/{len(self.test_data_loader)}')
            inputs = batched_sample['image'].to(self.device)
            labels = batched_sample['tag'].to(self.device)

            preds = self.model(inputs)
            preds_class = preds.argmax(dim=1)

            # Calculate accuracy
            running_test_acc += (preds_class == labels.data).float().mean()

            # Calculate true positives, flase positives etc.
            tp, fp, tn, fn = confusion_matrix(preds_class, labels.data)
            tps += tp
            fps += fp
            tns += tn
            fns += fn

        total_test_acc = round(
            (running_test_acc * 100 / len(self.test_data_loader)).item(), 2)
        return total_test_acc, tps, fps, tns, fns


def confusion_matrix(prediction, truth):
    """ Returns the confusion matrix for the values in the `prediction` and `truth`
    tensors, i.e. the amount of positions where the values of `prediction`
    and `truth` are
    - 1 and 1 (True Positive)
    - 1 and 0 (False Positive)
    - 0 and 0 (True Negative)
    - 0 and 1 (False Negative)
    """
    confusion_vector = prediction / truth
    # Element-wise division of the 2 tensors returns a new tensor which holds a
    # unique value for each case:
    #   1     where prediction and truth are 1 (True Positive)
    #   inf   where prediction is 1 and truth is 0 (False Positive)
    #   nan   where prediction and truth are 0 (True Negative)
    #   0     where prediction is 0 and truth is 1 (False Negative)

    true_positives = torch.sum(confusion_vector == 1).item()
    false_positives = torch.sum(confusion_vector == float('inf')).item()
    true_negatives = torch.sum(torch.isnan(confusion_vector)).item()
    false_negatives = torch.sum(confusion_vector == 0).item()

    return true_positives, false_positives, true_negatives, false_negatives
