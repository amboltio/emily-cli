# House Price Prediction API
In this demo we build an API that predicts house prices using linear regression. The accompanying guide can be found [here.](https://github.com/amboltio/emily-cli/wiki/House-price-prediction).

To run this demo, first make sure your Emily CLI is up and running: 
1. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/)
2. Run ```emily doctor``` to check all dependencies (CUDA is not required)

# Project setup
1. Download this demo by downloading or cloning the [emily-cli repo](https://github.com/amboltio/emily-cli).
1. run ```$ emily import ./house-price-prediction``` to initialize your local environment from the downloaded project folder
3. select a slim image
4. press `y` to mount data from local folder and give path: `./house-price-prediction/house-price-data`
5. run `$ emily open house-price-prediction`
6. The VSCode project opens

# Using the API
#### starting the API
1. Open the Run tab in VSCode
2. Select Emily API and click play
3. visit http://0.0.0.0:4242/api/health on your host machine to ensure that the API is running correctly

#### Make a prediction
1. Open a terminal on your host machine
2. Run:
```
curl --location --request POST 'http://0.0.0.0:4242/api/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sqft_living": "2000",
    "condition": "3",
    "zipcode": "98107",
    "model_path": "house-price-data/model.sav"}'
```
3. The API returns a price prediction

# Full Guide
You can see the full guide for builing this Emily Service [here.](https://github.com/amboltio/emily-cli/wiki/House-price-prediction) 
The guide covers:
- setting up the Emily project from scratch
- implementaiton of required classes for data processing, trainning, evaluating and predicting
- examples of how to update and evaluate the service with new data, via the /train and /evaluate endpoints
