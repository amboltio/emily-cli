
import os
import time
import torch

from torchvision import models


class Model(torch.nn.Module):
    """
    The Model class defines the Deep Learning model which should be used for training/evaluation/prediction.
    For detailed informaton and guidance on how to define a neural network, check out:
    https://pytorch.org/tutorials/recipes/recipes/defining_a_neural_network.html
    """

    def __init__(self):
        super().__init__()  # Inherit methods from the torch.nn.Module class which this class extends from

        # Number of different classes your model should be able to predict
        # Default is set to 2
        n_outputs = 2

        # The layers in the neural network. The below layers are only examples
        self.resnet = models.resnet18(pretrained=True, progress=True)

        # Disable gradient calculations on the layer/weights coming from ResNet. We will leave them as they are.
        for param in self.resnet.parameters():
            param.requires_grad = False

        self.fc1 = torch.nn.Linear(1000, 512)
        self.fc2 = torch.nn.Linear(512, 256)
        self.fc3 = torch.nn.Linear(256, n_outputs)
        self.activation_fn = torch.nn.ReLU()

        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.to(self.device)

    def forward(self, sample):
        """
        Steps which forwards the inputted sample into the layers of the model
        """
        x = self.resnet(sample)

        # relu stands for Rectified Linear Unit and is an Activation function.
        # For more information on activation functions in PyTorch,
        # check out: https://pytorch.org/docs/stable/nn.html#non-linear-activations-other
        x = self.fc1(x)
        x = self.activation_fn(x)
        x = self.fc2(x)
        x = self.activation_fn(x)
        output = self.fc3(x)

        return output


    def save_model(self, save_path, model_name: str):
        """
        Steps for saving the model instance.
        save_path : str
            The path where a trained model should be saved to
        """
        date_str = time.strftime("%Y-%m-%d-%H-%M-%S")

        # Make the path if it doesn't exists
        dir_name = os.path.dirname(save_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        save_name = os.path.join(save_path, date_str + "_" + model_name)

        # Save the model
        torch.save(self.state_dict(), save_path)

    def load_model(self, model_path):
        """
        Steps for loading a trained model
        model_path : str
            The path where the trained model is located and should be loaded from
        """
        if model_path is not None:
            self.model_path = model_path

        assert os.path.exists(
            self.model_path), f"Couldn't find a trained model at {self.model_path}"
        self.load_state_dict(torch.load(
            self.model_path, map_location=self.device))

    def __call__(self, sample):
        return self.forward(sample)

