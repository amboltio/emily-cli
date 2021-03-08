# Face Mask Detector demo

The following demonstration shows how to easily get started using a Face Mask Detector, implemented in the Emily API template provided by the [Emily](http://ambolt.io/emily) tool.

**Pre-requirements**
- [Emily](https://github.com/amboltio/emily-cli/#getting-started)
	- CUDA is **NOT** required for this project, but optional
- Python
- A web camera

## Quick start 
[**Full walkthrough**](https://github.com/amboltio/emily-cli/wiki/Face-mask-detection) of the implementation.

**Importing the Project**

1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
	* You can either clone or download as a ZIP (remember to unzip)
2. Open a terminal and locate the /emily-cli/demos folder
3. Run ```$ emily import ./face-mask-detector/face-mask-detector-api``` to import the Emily project and initialize the local environment
4. Press `y` to let Emily overwrite existing files. This updates the project to your current version of Emily.
5. Select a Full or PyTorch image
6. Press `n` to not mount data from a local folder
7. Choose if you want to run your project with GPU:
	* If you have CUDA enabled you can press `y` to run it with your GPU
	* Else, press `n`

**Running the API**

1. Run `$ emily open face-mask-detector-api` to open the project in VSCode
2. When VSCode opens up you might have to rebuild the container and reload PyLance 
3. Open api.py and press `F5`
	* This will host the API on port :4242
	* You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

**Launching the client**

1. Go to `./demos/face-mask-detector/face-mask-detector-client/` in your terminal
2. Start the client by executing `$ pyhton main.py` in your terminal
3. Go to `http://localhost:8000/` in your browser

Your project is now running in your browser!

**Learn more** 

If you want to learn more you should check out this in-depth walkthrough of how the API is implemented in Emily.
([Implementation walkthrough](https://github.com/amboltio/emily-cli/wiki/Face-mask-detection))
