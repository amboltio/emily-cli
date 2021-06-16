
import torch

import pandas as pd

from torch.utils.data.dataset import Dataset
from torch.utils.data.dataloader import DataLoader


def create_data_loader(csv_fp: str, batch_size: int, transform_fns=None, shuffle=False, num_workers=4):
    """
    Steps for creating a pytorch dataloader which is responsible for feeding a model with data
    during training/validation/evaluation. This method is used inside src/trainer.py and src/evaluator.py
    """

    # Instantiate dataset object
    dataset = CustomDataSet(
        dataset_csv=csv_fp,
        transform=transform_fns
    )

    # instantiate dataloader object
    data_loader = DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        pin_memory=True)

    return data_loader


class CustomDataSet(Dataset):

    def __init__(self, dataset_csv: str, transform=None):
        """
        The CustomDataset is an abstract class representing a dataset read from a csv file.
        The CustomDataset is used for creating a DataLoader object, which is responsible for feeding
        data to a model during e.g. training, validation and evaluation.

        The CustomDataset class inherits the PyTorch Dataset class and should override the following methods:
        - __getitem__ to support the indexing such that dataset[i] can be used to get ith sample of the data.

        For more information, check out: https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
        """
        self.df = pd.read_csv(dataset_csv)
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):

        if torch.is_tensor(idx):
            idx = idx.tolist()

        # TODO 1: Implement steps for reading data from the dataframe (self.df)
        data_columns = []
        data = self.df.iloc[idx, data_columns]

        # TODO 2: Implement steps for reading the ground truth aka tag/label
        label_column = None
        label = self.df.iloc[idx, label_column]

        # Apply transformations (check out src/transforms.py)
        if self.transform:
            data = self.transform(data)

        sample = {'data': data, 'label': label}

        return sample

