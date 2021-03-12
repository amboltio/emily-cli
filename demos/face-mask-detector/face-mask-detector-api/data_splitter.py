import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split_into_train_test_validation(X, y):
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)
    val_size = float(1 / 9)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size, random_state=1)

    print("Total samples:", len(X))
    print("Train samples:", len(X_train))
    print("Test samples:", len(X_test))
    print("Validation samples:", len(X_val))

    return X_train, y_train, X_test, y_test, X_val, y_val


def prepend_string_to_column(col: pd.Series, string: str):
    col = string + col
    return col


if __name__ == "__main__":

    # Read the annotations file with image names and corresponding mask/no-mask tag
    df = pd.read_csv("emily/annotations.csv")
    
    # Split the dataset into a train, test and validation dataset
    X = df["img_name"].values
    y = df[" mask"].values
    X_train, y_train, X_test, y_test, X_val, y_val = split_into_train_test_validation(X, y)

    # Column stack the image names and mask/no-mask tags again after split
    train = np.column_stack((X_train, y_train))
    test = np.column_stack((X_test, y_test))
    val = np.column_stack((X_val, y_val))

    # Convert into panda data frames
    train_df = pd.DataFrame(train, columns=["img_name", "mask"])
    test_df = pd.DataFrame(test, columns=["img_name", "mask"])
    val_df = pd.DataFrame(val, columns=["img_name", "mask"])

    # Add the path prefix to each of the image names in the image name column
    path_prefix = "emily/images/"
    train_df["img_name"] = prepend_string_to_column(train_df["img_name"], path_prefix)
    test_df["img_name"] = prepend_string_to_column(test_df["img_name"], path_prefix)
    val_df["img_name"] = prepend_string_to_column(val_df["img_name"], path_prefix)

    # Export the data frames as csv files
    train_df.to_csv("emily/train.csv", index=None)
    test_df.to_csv("emily/test.csv", index=None)
    val_df.to_csv("emily/val.csv", index=None)

    print(train_df["mask"].value_counts())
    print(test_df["mask"].value_counts())
    print(val_df["mask"].value_counts())
