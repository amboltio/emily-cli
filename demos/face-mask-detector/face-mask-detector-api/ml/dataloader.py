from torch.utils.data.dataloader import DataLoader

from ml.dataset import CustomDataset


class CustomDataLoader(DataLoader):
    """
    Dataloader class used for loading data during training/validation/evaluation
    The DatLoader object takes care of feeding samples to the model.
    """

    def __init__(self, csv_file, transform_fns, batch_size, shuffle=True, num_workers=4):
        dataset = CustomDataset(csv_file, transforms=transform_fns)
        super().__init__(dataset, batch_size=batch_size, num_workers=num_workers, shuffle=shuffle)

