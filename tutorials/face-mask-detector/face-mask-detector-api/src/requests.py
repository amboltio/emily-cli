
from pydantic import BaseModel


class TrainRequest(BaseModel):
    train_csv: str          # Path to the csv containing train samples
    val_csv: str            # Path to the csv containing validation samples
    batch_size: int         # The batch size during training
    epochs: int             # Number of time to iterate over entire training set during training
    save_path: str          # Where to save trained models to


class EvaluateRequest(BaseModel):
    test_csv: str       # Path to the csv containing test samples
    model_path: str     # Path to a trained model which should be evaluated
    batch_size: int     # The batch size during evaluation


class PredictRequest(BaseModel):
    img_path: str       # path to img to make predictions on
    model_path: str     # Path to a trained model which should make a prediction


class PredictWebcamRequest(BaseModel):
    image: str          # img to make predictions on
    model_path: str     # Path to a trained model which should make a prediction
