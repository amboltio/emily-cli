import pickle
from sklearn.linear_model import LinearRegression


class Model(LinearRegression):
    """
    The Model class defines the Machine Learning model which should be used for training/evaluation/prediction
    """

    def __init__(self):
        super().__init__()  # Inherit methods from the super class which this class extends from

    def forward(self, sample):
        return self.predict(sample)

    def save_model(self, save_path):
        opened_file = open(save_path, 'wb')
        pickle.dump(self, opened_file)
        opened_file.close()

        return True

    def load_model(self, model_path):
        opened_file = open(model_path, 'rb')
        loaded_model = pickle.load(opened_file)
        opened_file.close()

        return loaded_model

    def __call__(self, sample):
        return self.forward(sample)
