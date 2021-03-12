import torch
import os

from torchvision import models


class Model(torch.nn.Module):
    """
    The Model class defines the Machine Learning model which should be used for training/evaluation/prediction
    """

    def __init__(self):
        # Inherit methods from the super class which this class extends from
        super().__init__()
        
        self.resnet = models.resnet18(pretrained=True, progress=False)

        # Disable gradient calculations on the layer/weights coming from ResNet. We will leave them as they are.
        for param in self.resnet.parameters():
            param.requires_grad = False
        
        self.fc1 = torch.nn.Linear(1000, 512)
        self.act1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(512, 256)
        self.act2 = torch.nn.ReLU()
        self.fc3 = torch.nn.Linear(256, 2)

        # Set the device to GPU or CPU depending on what is available
        use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if use_cuda else "cpu")
        self.to(self.device)

    def forward(self, sample):
        """
        Steps which forwards the inputted sample into the model
        """
        x = self.resnet(sample)
        x = self.fc1(x)
        x = self.act1(x)
        x = self.fc2(x)
        x = self.act2(x)
        output = self.fc3(x)
        return output

    def save_model(self, save_path):
        """
        Implement steps for saving the model instance.
        e.g. using the pickle module (pickle.dump(model)) for sklearn models or torch.save(model) for PyTorch models
        save_path : str
            The path where a trained model should be saved to
        """
        torch.save(self.state_dict(), save_path)

    def load_model(self, model_path):
        """
        Implement steps for loading a trained model
        model_path : str
            The path where the trained model is located and should be loaded from
        """
        assert os.path.exists(model_path), f"Couldn't find a trained model at {model_path}"
        self.load_state_dict(torch.load(model_path, map_location=self.device))

    def __call__(self, sample):
        return self.forward(sample)
