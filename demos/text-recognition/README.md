# Text Recognition demo

This is a demonstration on how to implement text recognition(also called classification) in the Emily API template provided by the [Emily](http://ambolt.io/emily) tool.

**Pre-requirements**
- [Emily](https://github.com/amboltio/emily-cli/#getting-started)
	- CUDA is **NOT** required for this project, but optional

## Quick start 
[**Full walkthrough**](https://github.com/amboltio/emily-cli/wiki/Text-recognition) of the implementation.

**Importing the Project**

1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
	* You can either clone or download as a ZIP (remember to unzip)
2. Open a terminal and locate the /emily-cli/demos folder
3. Run ```$ emily import ./text-recognition/text-recognition-api``` to import the Emily project and initialize the local environment
4. Press `y` to let Emily overwrite existing files. This updates the project to your current version of Emily.
5. Select a Full or PyTorch image
6. Press `n` to not mount data from a local folder
7. Choose if you want to run your project with GPU:
	* If you have CUDA enabled you can press `y` to run it with your GPU
	* Else, press `n`

**Running the API**

1. Run `$ emily open text-recognition-api` to open the project in VSCode
	* Ignore `WARNING: Found orphan containers`
3. When VSCode opens up you might have to rebuild the container and reload PyLance 
4. Open api.py and press `F5`
	* This will host the API on port :4242
	* You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

**Launching the client**

1. Go to `./demos/sentiment-analysis/client/`
2. Launch the `index.html` file

Your project is now running in your browser!

**Learn more** 

If you want to learn more you should check out this in-depth walkthrough of how the API is implemented in Emily.
([Implementation walkthrough](https://github.com/amboltio/emily-cli/wiki/Text-recognition))
