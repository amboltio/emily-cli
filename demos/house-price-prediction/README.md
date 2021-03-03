# House Price Prediction API
In this demo we wil run an API that predicts house prices using linear regression. See the [full guide](https://github.com/amboltio/emily-cli/wiki/House-price-prediction) if you want to build this service from scratch.

To run this demo, first make sure your Emily CLI is up and running: 
1. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/))
2. Run ```emily doctor``` to check all dependencies (CUDA is not required)

# Project setup
1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
2. Open a terminal and locate the /emily-cli/demos folder
3. Run ```$ emily import ./house-price-prediction``` to import the Emily project and initialize the local environment
4. Select a slim image
5. Press `y` to mount data from local folder and give path: `./house-price-prediction/house-price-data`
6. Run `$ emily open house-price-prediction` to open the project in VSCode


# Using the API
#### Starting the API
1. Press `F5` in VSCode to run api.py
3. Visit http://127.0.0.1:4242/api/health on your host machine to ensure that the API is running correctly (VSCode will map to a different port if 4242 is already taken)

#### Make a prediction
1. Open a terminal on your host machine
2. Run:
```
curl --location --request POST 'http://127.0.0.1:4242/api/predict' \
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
- Setting up the Emily project from scratch
- Implementaiton of required classes for data processing, training, evaluating and predicting
- Examples of how to update and evaluate the service with new data, via the /train and /evaluate endpoints
