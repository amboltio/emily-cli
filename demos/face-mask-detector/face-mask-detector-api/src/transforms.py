
from torchvision.transforms import transforms

"""
For a comprehensive list and guide on pytorch transforms check out:
https://pytorch.org/vision/stable/transforms.html
"""

RESIZE_W = 256
RESIZE_H = 256


def train_transforms():
    """
    OPTIONAL: Implement transforms/preprocessing steps
    which should be performed on the data during training
    """
    return transforms.Compose([
        transforms.RandomHorizontalFlip(0.5),
        transforms.ColorJitter(brightness=1, contrast=0.5, saturation=1, hue=0.5),
        transforms.RandomAffine(degrees=45, scale=(0.5, 1), shear=(0, 25)),
        transforms.Resize(size=(RESIZE_H, RESIZE_W)),
        transforms.ToTensor()
    ])


def test_transforms():
    """
    OPTIONAL: Implement transforms/preprocessing steps
    which should be performed on the data during testing/evaluation
    """
    return transforms.Compose([
        transforms.Resize(size=(RESIZE_H, RESIZE_W)),
        transforms.ToTensor()
    ])


def validation_transforms():
    """
    OPTIONAL: Implement transforms/preprocessing steps
    which should be performed on the data during validation
    """
    return test_transforms()

