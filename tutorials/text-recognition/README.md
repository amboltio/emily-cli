# Text Recognition 📝🧐

This guide explains how to run an **text recognition** to responde to **pizza ordering requests** using the Emily CLI. 

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
4. Run ```$ emily open ./text-recognition/text-recognition-api``` to import the Emily project
5. Select a slim image
6. Select the Visual Studio Code editor  
	* **Note:** After Visual Studio Code is opened you might be asked to rebuild the container and/or reload PyLance - do so.


## Running the API
1. Open api.py and press `F5` or press the green _play_ icon in the top right 
	* This will host the API on port _4242_
2. You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

## Interacting with the API
### Launch the client
1. Go to `./tutorials/text-recognition/client/`
2. Launch the `index.html` file
      * Your project is now running in your browser!
3. Write acting as a danish pizza vendor e.g. "hvad skulle det være" and get a text class and response.

## Learn more 
Do you want to learn more on how the **Text Recognition** is implemented Emily, check out this in-depth walkthrough:
- [Text Recognition walkthrough](https://github.com/amboltio/emily-cli/wiki/Sentiment-analysis)
- Get more information on the [Emily Platform](https://ambolt.io/emily-ai/)
