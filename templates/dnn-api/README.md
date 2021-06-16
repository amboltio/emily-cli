
## Description:
Welcome to your Emily API and thanks you for utilizing the PyTorch Deep Learning template. 

This template contains the main pars of a standard PyTorch neural network model, for setting up training of a model, evaluation of a trained model and making predictions using a trained model. 

In order to be able to start training your first model, the following steps needs to be taken:

## Steps:

Firstly, we need to make sure your dataset can be read correctly during training, validation and evaluation.:

1. Navigate to the `CustomDataSet` class inside src/data_utilities.py
    * **TODO 1**: Make sure your data is read correctly inside the `__getitem__()`-method
    * **TODO 2**: Make sure your labels/tags  are read correclty inside the `__getitem__()`-method
    * If you are not sure what to do, more information on data loading in PyTorch can be found at : https://pytorch.org/tutorials/beginner/data_loading_tutorial.html

Secondly, the layers of the neural network model needs to be fully defined, to make sure it corresponds to your task:

2. Navigate to the `Model` class inside src/model.py
    * **TODO 1**: Set the number of classes which your model should be able to predict in the `n_outputs` variable in the `__init__()`- method. 
    * **TODO 2a**: Define the layers of your CNN or use the default layers.  
    * **TODO 2b**: Make sure to use the layers defined in the `__init__()`-method in your model's `forward()`-method. 

Finally, we want to test wether the training of a model works:

3. Navigate to the train notebook inside notebooks/train.ipynb
    * Run the notebook clicking the double play arrows ('run all cells') at the top of the notebook
