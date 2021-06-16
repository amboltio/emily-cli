
from torchvision.transforms import transforms

"""
For a comprehensive list and guide on pytorch transforms check out:
https://pytorch.org/vision/stable/transforms.html
"""


def train_transforms():
    """
    OPTIONAL: Implement transforms/preprocessing steps
    which should be performed on the data during training
    """
    return transforms.Compose([
        transforms.ToTensor()
    ])


def test_transforms():
    """
    OPTIONAL: Implement transforms/preprocessing steps
    which should be performed on the data during testing/evaluation
    """
    return transforms.Compose([
        transforms.ToTensor()
    ])


def validation_transforms():
    """
    OPTIONAL: Implement transforms/preprocessing steps
    which should be performed on the data during validation
    """
    return transforms.Compose([
        transforms.ToTensor()
    ])

