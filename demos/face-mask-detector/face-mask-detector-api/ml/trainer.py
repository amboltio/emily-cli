import torch
import os
import pathlib
import time

from ml.model import Model
from ml.dataloader import CustomDataLoader
from ml.evaluator import confusion_matrix
from ml.transforms import train_transforms, validation_transforms


class Trainer:
    """
    The Trainer class is used for training a model instance based on the Model class found in ml.model.py.
    In order to get started with training a model the following steps needs to be taken:
    1. Define the Model class in ml.model.py
    2. Prepare train data on which the model should be trained with by implementing the _read_train_data() function and
    the _preprocess_train_data() function
    """

    def __init__(self,
                 train_csv: str,
                 val_csv: str,
                 batch_size: int, learning_rate: float, epochs: int, seed: int,
                 save_path: str):

        use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if use_cuda else "cpu")

        # creates an instance of the Model class (see guidelines in ml.model.py)
        self.model = Model()

        # Set training parameters
        self.batch_size = batch_size if batch_size else 32
        self.learning_rate = learning_rate if learning_rate else 0.001
        self.epochs = epochs if epochs else 10
        self.seed = seed
        self.num_workers = 8

        self.train_csv = train_csv
        self.val_csv = val_csv

        print("Save path", save_path)
        self.save_path = save_path
        if not os.path.exists(self.save_path):
            pathlib.Path(self.save_path).mkdir(parents=True, exist_ok=True)

    def train(self):
        """
        Starts the training of a model based on data loaded by the self._load_train_data function
        """

        # Instantiate pyTorch dataloaders
        train_data_loader = CustomDataLoader(
            self.train_csv, train_transforms(), self.batch_size, shuffle=True, num_workers=self.num_workers)
        validation_data_loader = CustomDataLoader(
            self.val_csv, validation_transforms(), self.batch_size, shuffle=True, num_workers=self.num_workers)

        # Define loss function, optimizer and learning rate scheduler
        loss_function = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.9)

        train_losses = []
        train_accs = []
        val_losses = []
        val_accs = []
        best_acc = 0

        # Implement steps which trains a model
        print(f"Starting training. Will run for {self.epochs} epochs")
        torch.manual_seed(self.seed)
        for epoch in range(0, self.epochs):
            
            running_train_loss = 0.
            running_train_acc = 0.
            start_time = time.time()
            print('Epoch {}/{}:'.format(epoch + 1, self.epochs), flush=True)

            # Set the model's mode to training
            self.model.train()
            for idx, (batched_sample) in enumerate(train_data_loader):
                
                if (idx + 1) % 10 == 0:
                    print(f'Processing batch {idx + 1}/{len(train_data_loader)}')

                # Read images and corresponding tags for the current batch
                inputs = batched_sample['image'].to(self.device)
                labels = batched_sample['tag'].to(self.device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward + backward + optimize
                preds = self.model(inputs)
                preds_class = preds.argmax(dim=1)
                loss_value = loss_function(preds, labels)
                loss_value.backward()
                optimizer.step()

                # Calculate batch loss and accuracy
                running_train_loss += loss_value.item()
                running_train_acc += (preds_class ==
                                      labels.data).float().mean()

            train_loss = running_train_loss / len(train_data_loader)
            train_acc = running_train_acc / len(train_data_loader)
            train_losses.append(train_loss)
            train_accs.append(train_acc)
            lr_scheduler.step()

            end_time = time.time()
            print(f"Epoch took {str(round(end_time - start_time, 2))}")

            # Set the model's mode to evaluation (mean gradients will not be calculated which speeds up the process)
            self.model.eval()
            running_val_loss = 0.
            running_val_acc = 0.
            tps, fps, tns, fns = 0, 0, 0, 0
            print("Evaluting model on validation set...")
            for idx, (batched_sample) in enumerate(validation_data_loader):
                inputs = batched_sample['image'].to(self.device)
                labels = batched_sample['tag'].to(self.device)

                preds = self.model(inputs)
                loss_value = loss_function(preds, labels)
                preds_class = preds.argmax(dim=1)

                # # Calculate batch loss and accuracy
                running_val_loss += loss_value.item()
                running_val_acc += (preds_class == labels.data).float().mean()

                # Calculate true positives, flase positives etc.
                tp, fp, tn, fn = confusion_matrix(preds_class, labels.data)
                tps += tp
                fps += fp
                tns += tn
                fns += fn

            print("tps", tps, "tns", tns, "fps", fps, "fns", fns)
            val_loss = running_val_loss / len(validation_data_loader)
            val_acc = running_val_acc / len(validation_data_loader)
            val_losses.append(val_loss)
            val_accs.append(val_acc)

            # Save the model if the accuracy is better
            if val_acc > best_acc:
                best_acc = val_acc
                model_name = f'resnet_18_epoch_{epoch+1}_acc_{round(best_acc.item() * 100, 2)}.pth'
                self.model.save_model(os.path.join(self.save_path, model_name))

            print('train Loss: {:.4f} train Acc: {:.4f} test loss: {:.4f} test acc: {:.4f}'.format(
                train_loss, train_acc, val_loss, val_acc), flush=True)

        # return the trained model
        return self.model, train_losses, val_losses, train_accs, val_accs


    def __call__(self, request):
        return self.train(request)
