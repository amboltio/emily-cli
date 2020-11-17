import os
import json
import matplotlib.pyplot as plt
import torch
from torch import nn


class Model(nn.Module):
    """
    The Model class defines the Machine Learning model which should be used for training/evaluation/prediction
    """

    def __init__(self, input_size, output_size):
        """Defines a model with 3 fully connected layers.  
        First layer: input size -> 128 neurons  
        Second layer: 128 -> 64 neurons  
        Third layer: 64 -> output size

        The model also contrains dropout and performs ReLU activation between
        layers 1-2 and 2-3. Softmax can be applied to the output during inference
        if class probabilies are needed.
        """
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, output_size)
        self.dl = nn.Dropout(p=0.5)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.dl(self.relu(self.fc1(x)))
        x = self.dl(self.relu(self.fc2(x)))
        x = self.fc3(x)
        return x

    def save_model(model_dir, meta_data, optimizer):
        '''
        saves both the model state dict and model checkpoint  
        '''
        model_state_dict_name = 'model_state_dict.pt'
        model_checkpoint_name = 'model_checkpoint.pt'

        # saves model state dict
        torch.save(self.state_dict(), os.path.join(model_dir, model_state_dict_name))

        # saves model checkpoint
        torch.save({
                'epoch': meta_data['epoch'],
                'model_state_dict': self.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': meta_data['loss'],
                }, os.path.join(model_dir, model_checkpoint_name))

        # save meta data
        with open(os.path.join(model_dir, 'meta.json'), 'w') as fp:
            json.dump(meta_data, fp, indent=4)

    def load_model(model_dir, load_method=None):
        """Takes model directory and load method and returns a model

        Parameters:
        model_dir (str): model directory
        model_dir (str): load method - can be: "state dict" or "checkpoint"

        Returns:
        PyTorch model
        """
        if load_method is None:
            print('No load method selected. Defaulting to loading from state dict.')
            load_method = 'state dict'

        with open(os.path.join(model_dir, 'meta.json'), 'r') as fp:
            meta_data = json.load(fp)
        if load_method == 'state dict':
            self.load_state_dict(torch.load(os.path.join(model_dir, 'model_state_dict.pt')))
        elif load_method == 'checkpoint':
            checkpoint = torch.load(os.path.join(model_dir, 'model_checkpoint.pt'))
            self.load_state_dict(checkpoint['model_state_dict'])

    def save_training_diagram(model_dir, acc_history, loss_history):
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
        # plot acc history
        axes[0].plot(acc_history, 'r')
        axes[0].set_title('model accuracy')
        axes[0].set_ylabel('accuracy')
        axes[0].set_xlabel('epoch')
        # plot loss history
        axes[1].plot(loss_history, 'b')
        axes[1].set_title('model loss')
        axes[1].set_ylabel('loss')
        axes[1].set_xlabel('epoch')

        # save figure
        fig.savefig(os.path.join(model_dir, 'train.jpg'), transparent=False)

    def __call__(self, sample):
        return self.forward(sample)

