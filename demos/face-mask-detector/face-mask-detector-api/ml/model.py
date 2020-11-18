import torch
from torch import nn
from torch.nn import functional as F


class Model(torch.nn.Module):
    """
    The Model class defines the Machine Learning model which should be used for training/evaluation/prediction
    """

    def __init__(self):
        super().__init__()  # Inherit methods from the super class which this class extends from
        self.conv1 = nn.Conv2d(3, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.conv3 = nn.Conv2d(64, 128, 3, 1)
        self.conv4 = nn.Conv2d(128, 128, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(4608, 128)
        self.fc3 = nn.Linear(128, 2)

    def forward(self, sample):
        # First layer
        x = self.conv1(sample)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)

        # Second layer
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)

        # Third layer
        x = self.conv3(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)

        # Fourth layer
        x = self.dropout1(x)
        x = self.conv4(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)

        # Fifth layer
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)

        # Final layer
        x = self.dropout2(x)
        x = self.fc3(x)
        output = F.log_softmax(x, dim=1)
        return output

    def save_model(self, save_path):
        """
        Steps for saving the model instance.
        save_path : str
            The path where a trained model should be saved to
        """
        torch.save(self.state_dict(), save_path)

    def load_model(self, model_path):
        """
        Steps for loading a trained model
        model_path : str
            The path where the trained model is located and should be loaded from
        """
        self.load_state_dict(torch.load(model_path))

    def __call__(self, sample):
        return self.forward(sample)

