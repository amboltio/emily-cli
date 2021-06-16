

class Model():
    """
    The Model class defines the Machine Learning model which should be used for training/evaluation/prediction
    TODO 1: Specify an appropriate Machine Learning model which the Model class should extend from
    ------
    E.g. 'class Model(sklearn.linear_model.LinearRegression)' or 'class Model(torch.nn.Module)'
    """

    def __init__(self):
        super().__init__()  # Inherit methods from the super class which this class extends from

    def forward(self, sample):
        """
        TODO 2:Implement the steps which forwards the inputted sample into the model
        e.g. super().__call__(), self.predict(), self.predict_proba etc.
        The implementation depends on the Machine Learning model this Model class extends
        """
        return sample

    def save_model(self, save_path):
        """
        TODO 3: Implement steps for saving the model instance.
        e.g. using the pickle module (pickle.dump(model)) for sklearn models or torch.save(model) for PyTorch models
        save_path : str
            The path where a trained model should be saved to
        """

    def load_model(self, model_path):
        """
        TODO 4: Implement steps for loading a trained model
        e.g. using the pickle module (pickle.load(model)) for sklearn models or torch.load for PyTorch models'
        model_path : str
            The path where the trained model is located and should be loaded from
        """

    def __call__(self, sample):
        return self.forward(sample)

