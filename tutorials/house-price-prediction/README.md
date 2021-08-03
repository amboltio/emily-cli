# House Price Predictor 🏠📈

This guide explains how run **linear regression** to **predict house prices** using the Emily CLI.

## Prerequisites
This guide requires that you have [Emily](https://ambolt.io/emily-ai/) installed on your computer.
- Download [Emily](https://github.com/amboltio/emily-cli/releases/latest) for your OS
- Install Emily:
  - [Windows install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily-on-Windows)
  - [Linux install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily-on-Linux)
  - [Mac install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-emily-on-Mac)

## Importing the Project
1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
	* You can either clone or download as a ZIP (remember to unzip)
2. Open a terminal and locate the _/emily-cli/tutorials_ folder
3. Run ```$ emily open ./house-price-prediction/house-price-prediction-api``` to import the Emily project
4. Select a slim image
5. Select the Visual Studio Code editor  
	* **Note:** After Visual Studio Code is opened you might be asked to rebuild the container and/or reload PyLance - do so.

## Running the API
1. Open api.py and press `F5` or press the green _play_ icon in the top right 
	* This will host the API on port _4242_
2. You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

## Interacting with the API
1. To get a prediction execute the following in your terminal:   
`$ curl --header "Content-Type: application/json" --request POST --location http://localhost:4242/api/predict --data "{\"sqft_living\":\"2000\",\"condition\":\"3\",\"yr_built\":\"1987\",\"model_path\":\"house-price-data/model.sav\"}"`
2. Play around with `sqft_living`, `condition`, and `yr_built` to get more predictions

## Learn more 
Do you want to learn more on how the **House Price Predictor** is implemented Emily, check out this in-depth walkthrough:
- [House Price Predictor walkthrough](https://github.com/amboltio/emily-cli/wiki/House-price-prediction)
- Get more information on the [Emily Platform](https://ambolt.io/emily-ai/)


