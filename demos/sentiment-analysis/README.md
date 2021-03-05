# Sentiment Analysis demo

This demo contains an Emily microservice for conducting sentiment analysis, and a web client that consumes the API exposed by the microservice. 

**Pre-requirements**
- [Emily](https://ambolt.io/emily-ai/) **- installer**
	- [Emily setup guide](https://github.com/amboltio/emily-cli/)
	- CUDA is **NOT** required for this project

## Quick start 
[**Full walkthrough**](https://github.com/amboltio/emily-cli/wiki/Sentiment-analysis) of the implementation.

**Importing the Project**

1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
	* You can either clone or download as a ZIP (remember to unzip)
2. Open a terminal and locate the /emily-cli/demos folder
3. Run ```$ emily import ./sentiment-analysis/sentiment-anylysis-api``` to import the Emily project and initialize the local environment
4. Press `y` to let Emily overwrite existing files. This updates the project to your current version of Emily.
5. Select a slim image
6. Press `y` to mount data from local folder and give path: `./sentiment-analysis/sentiment-analysis-api/data`

**Running the API**

1. Run `$ emily open sentiment-analysis-api` to open the project in VSCode
	* Ignore `WARNING: Found orphan containers`
2. When VSCode opens up you might have to rebuild the container and reload PyLance 
3. Open api.py and press `F5`
	* This will preprocess the training data and host the API on port :4242
	* You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

**Launching the client**

1. Go to `demos/sentiment-analysis/sentiment-analysis-client/`
2. Launch the `index.html` file

Your project is now running in your browser!

**Learn more** 

If you want to learn more you should check out this in depth walkthrough of how the API is implemented in Emily.
([Implementation walkthrough](https://github.com/amboltio/emily-cli/wiki/Sentiment-analysis))
