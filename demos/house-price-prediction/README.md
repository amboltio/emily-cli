# House Price Prediction API
This demo shows how to easily predict house prices using linear regression in the Emily API template provided by the [Emily](http://ambolt.io/emily) CLI tool.
The accompanying guide can be found at [https://github.com/amboltio/emily-cli/wiki/House-price-prediction](https://github.com/amboltio/emily-cli/wiki/House-price-prediction).

To run this demo, first download the demo files from this folder, by downloading or cloning the [emily-cli repository](https://github.com/amboltio/emily-cli). 

Make sure you have Emily CLI and its dependencies installed:
1. Download the Emily CLI from [here](http://ambolt.io/emily)
2. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily))
3. Run ```emily doctor``` from your terminal (Bash or PowerShell) to let Emily help you install all dependencies

When all dependencies are installed, import the project into Emily by typing e.g. ```emily import ~/Downloads/house-price-prediction``` if you downloaded the demo into your Downloads folder. When importing, say no to GPU and CUDA support, and when prompted for the path to ```/workspace/data```, give the path to the ```house-price-data``` folder in the demo.
After the project has been imported into Emily, open it by typing ```emily import house-price-prediction```.

# Using the API
Start the House Price Prediction API by executing the following command **from the terminal in VSCode**:
```
python api.py
```

By default, when the API is running it will be accessible at http://0.0.0.0:4242.
To test if the House Price Prediction API is running, try entering http://0.0.0.0:4242/api/health in your browser.
Training, evaluating, and predicting using the model is done by sending POST requests in JSON format to the train, evaluate, and predict endpoints, respectively.
This can be done using e.g. [Postman](https://www.postman.com/) or [curl](https://curl.se/).

To train, send a POST request to `http://0.0.0.0:4242/api/train` with key/value pairs `dataset_path=data/train_data.csv` and `save_path=data/model.sav`. You should get an output indicating succes:
```
{
    "result": true
}
```

To evaluate, send a POST request to `http://0.0.0.0:4242/api/evaluate` with key/value pairs `dataset_path=data/test_data.csv` and `model_path=data/model.sav`. This will give you the mean absolute error of the model:
```
{
    "result":172375.82537201577
}
```

To predict, send a POST request to `http://0.0.0.0:4242/api/predict` with key/value pairs `sqft_living=2000`, `condition=3`, `zipcode=98107`, and `model_path=data/model.sav`. This will ask the model to predict the house price of a 2000-square foot house in mediocre condition in the area with zip code 98107. You will get the following output.
```
{
    "result": "$518379.0194906518"
}
```

## Requirements:
- [Emily](http://ambolt.io/emily)
