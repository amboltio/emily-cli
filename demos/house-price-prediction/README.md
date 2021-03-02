# House Price Prediction API
In this demo we build an API that predicts house prices using linear regression. The accompanying guide can be found [here.](https://github.com/amboltio/emily-cli/wiki/House-price-prediction).

To run this demo, first make sure your Emily CLI is up and running: 
1. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/)
2. Run ```emily doctor``` to check all dependencies (CUDA is not required)
3. Download this demo, by downloading or cloning the [emily-cli repo](https://github.com/amboltio/emily-cli).

# Project setup
1. run ```$ emily import /house-price-prediction``` to initialize your local environment
3. select a slim image
4. press `y` to mount data from local folder and give path: `./house-price-prediction/house-price-data`
5. run `$ emily open house-price-prediction`
6. The VSCode project opens

# Using the API
#### starting the API
1. open the Run tab
2. Select Emily API and click play
3. visit http://0.0.0.0:4242/api/health to ansure that API is running

#### call the API
1. 
 
TODO: curl examples. People who use postman knows about postman.

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
