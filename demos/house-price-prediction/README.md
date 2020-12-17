# House Price Prediction API
This demo shows how to easily predict house prices using linear regression in the Emily API template provided by the [Emily](http://ambolt.io/emily) CLI tool.
The accompanying guide can be found at [https://github.com/amboltio/emily-cli/wiki/House-price-prediction](https://github.com/amboltio/emily-cli/wiki/House-price-prediction).

To run this demo, first download the demo files from this folder, by downloading or cloning the [emily-cli repository](https://github.com/amboltio/emily-cli). 

Make sure you have Emily CLI and its dependencies installed:
1. Download the Emily CLI from [here](http://ambolt.io/emily)
2. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily))
3. Run ```emily doctor``` from your terminal (Bash or PowerShell) to let Emily help you install all dependencies

When all dependencies are installed, open VSCode and from VSCode open the downloaded house-price-prediction folder. 

**Attention**: Make sure the house-price-prediction folder is opened as a Docker container. If Emily is installed correctly, VSCode will prompt whether it should **"Re-open [the folder] in Container"**. Make sure to press **"OK"** to this.

# Using the API
Start the House Price Prediction API by executing the following command **from the terminal in VSCode**:
```
python api.py
```

By default, when the API is running it will be accessible at http://0.0.0.0:4242.
To test if the House Price Prediction API is running, try entering http://0.0.0.0:4242/api/health in your browser.
Training, evaluating, and predicting using the model is done by sending POST requests to the train, evaluate, and predict endpoints, respectively.
This can be done using e.g. [Postman](https://www.postman.com/) or [curl](https://curl.se/).

To train, send a POST request to `http://0.0.0.0:4242/api/train` with key/value pairs `dataset_path=data/train_data.csv` and `save_path=data/model.sav`. You should get an output indicating succes:
```
{
    "success": true
}
```

To evaluate, send a POST request to `http://0.0.0.0:4242/api/evaluate` with key/value pairs `dataset_path=data/test_data.csv` and `model_path=data/model.sav`. This will give you the mean absolute error of the model:
```
{
    "result": 4.0203266061645495
}
```

To predict, send a POST request to `http://0.0.0.0:4242/api/predict` with key/value pairs `sample=6` and `model_path=data/model.sav`. This will ask the model to predict the house price of a 6-room house. You will get the following output.
```
{
    "prediction": "$19588.8762740132"
}
```

## Requirements:
- [Emily](http://ambolt.io/emily)
