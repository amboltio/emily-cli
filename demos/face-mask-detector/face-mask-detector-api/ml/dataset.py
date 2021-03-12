import torch

import pandas as pd
import numpy as np

from skimage import io
from PIL import Image
from torch.utils.data.dataset import Dataset


class CustomDataset(Dataset):

    def __init__(self, csv_file: str, transforms=None):
        # Read the csv file as a panda's data frame
        assert csv_file.endswith(
            ".csv"), f'Expected {csv_file} to be a .csv file'
        self.data_frame = pd.read_csv(csv_file)

        # Set the transforms (preprocessing steps defined by torchvision.transforms
        self.transforms = transforms

    def __len__(self):
        return len(self.data_frame)

    def __getitem__(self, item):
        # Read the img name from the dataframe. Asserting the first column in the data frame contains this
        img_name = self.data_frame.iloc[item, 0]

        # Load and convert the image into a PIL Image
        image = io.imread(img_name)

        # Mitigate the fact that some images comes in gray-scale (only has 1 depth dimension)
        if len(image.shape) == 2:
            image = x = np.dstack((image, image, image))

        image = Image.fromarray(image)

        # Preprocess the image according the given transforms
        if self.transforms:
            image = self.transforms(image)

        # Read the tag from the dataframe. Asserting the second column in the data frame contains this
        tag = self.data_frame.iloc[item, 1]

        # Convert tag into a numeric value and then into a Torch tensor object
        if "True" in tag:
            tag = 1
        else:
            tag = 0
        
        tag = torch.tensor(tag)

        sample = {'image': image, 'tag': tag}
        return sample
