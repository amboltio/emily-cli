# House Price Predictor 🏠📈

This guide explains how run **linear regression** to **predict house prices** using the Emily CLI.

<div align="center">
<img src="https://github.com/amboltio/emily-cli/blob/main/tutorials/house-price-prediction/house-price-prediction-client/house-price.png" alt="House Price Predictor" height="500"/>
</div>

## Prerequisites
1. This guide requires that you have [Emily](https://ambolt.io/emily-ai/).
Hence you must [download](https://github.com/amboltio/emily-cli/releases/latest) and [install](https://github.com/amboltio/emily-cli/wiki/Install-Emily) it.

## Importing the Project
1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
	* You can either clone or download as a ZIP (remember to unzip)
2. Open a terminal and locate the `tutorials` folder
3. Run ```$ emily open ./house-price-prediction/house-price-prediction-api``` to import the Emily project
4. Select the Visual Studio Code editor  
	* **Note:** After Visual Studio Code is opened you might be asked to rebuild the container and/or reload PyLance - do so.

## Running the API
1. Open api.py and press `F5` or press the green _play_ icon in the top right 
	* This will host the API on port _4242_
	* (Alternatively use ```$ python api.py``` in the Visual Studio Code terminal)
2. You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

## Interacting with the API
### Launch the client
1. Go to `tutorials/house-price-prediction/house-price-prediction-client/`
2. Launch the `index.html` file
      * Your project is now running in your browser!
3. Play around with `square feet`, `condition`, and `year build` to get predictions.

<!--
## Learn more 
Do you want to learn more on how the **House Price Predictor** is implemented Emily, check out this in-depth walkthrough:
- [House Price Predictor walkthrough](https://github.com/amboltio/emily-cli/wiki/House-price-prediction)
- Get more information on the [Emily Platform](https://ambolt.io/emily-ai/)
-->


