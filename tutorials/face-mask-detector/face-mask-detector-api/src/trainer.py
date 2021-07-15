
import torch
import time

from src.model import Model
from src.engine import train_step, validation_step
from src.data_utilities import create_data_loader
from src.transforms import train_transforms, validation_transforms
from src.requests import TrainRequest

class Trainer:
    """
    The Trainer class is used for training a model instance based on the Model class found in src.model.py.
    """

    def __init__(self, request: TrainRequest):

        # Set the path to the csv files containing the training- and the validation datasets
        self.train_csv = request.train_csv
        self.val_csv = request.val_csv

        # Set training parameters
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.epochs = request.epochs
        self.batch_size = request.batch_size

        # Set the path where to save trained models to
        self.save_path = request.save_path

        # Instantiate a model object (see src/model.py)
        self.model = Model()
        # Sets the seed used for generating random weights
        torch.manual_seed(42)

    def train(self):
        """
        Starts the training of a model
        """

        # Create the pytorch dataLoaders which takes care of feeding samples to the model
        train_data_loader = create_data_loader(
            csv_fp=self.train_csv,
            batch_size=self.batch_size,
            transform_fns=train_transforms(),
            shuffle=True,
            num_workers=4
        )

        validation_data_loader = create_data_loader(
            csv_fp=self.val_csv,
            batch_size=self.batch_size,
            transform_fns=validation_transforms(),
            shuffle=True,
            num_workers=4
        )

        # Define the loss-function used for calculating the models loss during training
        # Checkout https://pytorch.org/docs/stable/nn.html#loss-functions
        loss_fn = torch.nn.CrossEntropyLoss()

        # Define the optimizer used for performing gradient descent (adjusting weights and biases during training)
        # Checkout: https://pytorch.org/docs/stable/optim.html
        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)

        # Define the scheduler used for dynamically adjusting the learning rate during training
        # Checkout: https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate
        scheduler = torch.optim.lr_scheduler.StepLR(
            optimizer, step_size=10, gamma=0.9)

        # Steps which trains a model
        print(f"Starting training. Will run for {self.epochs} epochs")
        best_val_acc = 0
        best_val_acc_model = None

        for epoch in range(0, self.epochs):

            train_accuracy, train_loss = train_step(
                epoch, train_data_loader, loss_fn, optimizer, scheduler)

            val_accuracy, val_loss = validation_step(
                validation_data_loader, loss_fn)

            print('train Loss: {:.4f} train Acc: {:.4f} test loss: {:.4f} test acc: {:.4f}'.format(
                train_loss, train_accuracy, val_loss, val_accuracy), flush=True)

            # Save the model
            date_str = time.strftime("%Y-%m-%d-%H-%M-%S")
            model_name = f'{date_str}_model_{epoch+1}_acc_{round(val_accuracy * 100, 2)}.pth'
            self.model.save_model(
                save_path=self.save_path, model_name=model_name)

            if val_accuracy > best_val_acc:
                best_val_acc = val_accuracy
                best_val_acc_model = model_name

        return best_val_acc, best_val_acc_model

    def __call__(self):
        return self.train()

