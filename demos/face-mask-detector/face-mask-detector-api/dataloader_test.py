from ml.dataloader import CustomDataLoader
from ml.transforms import train_transforms


if __name__ == "__main__":

    train_csv = "emily/train.csv"
    train_data_loader = CustomDataLoader(train_csv, train_transforms(), 1, shuffle=True, num_workers=8)
