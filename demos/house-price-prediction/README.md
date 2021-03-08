# House Price Prediction demo

In this demo we will run an API that predicts house prices using linear regression.

**Pre-requirements**
- [Emily](https://github.com/amboltio/emily-cli/#getting-started)
	- CUDA is **NOT** required for this project

## Quick start 
[**Full walkthrough**](https://github.com/amboltio/emily-cli/wiki/House-price-prediction) of the implementation.

**Importing the Project**

1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
	* You can either clone or download as a ZIP (remember to unzip)
2. Open a terminal and locate the /emily-cli/demos folder
3. Run ```$ emily import ./house-price-prediction/house-price-prediction-api``` to import the Emily project and initialize the local environment
4. Press `y` to let Emily overwrite existing files. This updates the project to your current version of Emily.
5. Select a slim image
6. Press `y` to mount data from local folder and give path: `./house-price-prediction/house-price-prediction-api/house-price-data`

**Running the API**

1. Run `$ emily open house-price-prediction-api` to open the project in VSCode
2. When VSCode opens up you might have to rebuild the container and reload PyLance 
3. Open api.py and press `F5`
	* This will host the API on port :4242
	* You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

**Make Predictions**

1. Execute the following in your terminal: `$ curl --header "Content-Type: application/json" --request POST --location http://localhost:4242/api/predict --data "{\"sqft_living\":\"2000\",\"condition\":\"3\",\"yr_built\":\"1987\",\"model_path\":\"house-price-data/model.sav\"}"`  to get a prediction
	* You can play around with the sqft_living, condition, and year built to get more predictions


**Learn more** 

If you want to learn more you should check out this in depth walkthrough of how the API is implemented in Emily.
([Implementation walkthrough](https://github.com/amboltio/emily-cli/wiki/House-price-prediction))


