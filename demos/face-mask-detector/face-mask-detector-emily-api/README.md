
# Face Mask Detector API

The Face Mask Detector API is implemented using the [Emily](http://ambolt.io/emily) CLI tool and it's API template.

To run the Face Mask Detector API, first download or clone the [face-mask-detector folder](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector) 

Make sure you have Emily and it's dependencies installed:
1. Download the Emily installer from [here](http://ambolt.io/emily)
2. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily)
3. Run ```emily doctor``` from your terminal (Bash or PowerShell) to make sure any missing dependencies are installed

When all dependencies are installed, open VSCode and from VSCode open the face-mask-detector-emily-api folder. 

Attention: Make sure the folder is opened as a container. VSCode will prompt whether it should **"Re-open as a container"**. Make sure to press **"OK"** to this.

Finally, start the Face Mask Detector API by executing the following command **from the terminal in VSCode**:
```
python api.py
```

By default, your API will be accessible at http://127.0.0.1:4242. 

To test if the Face Mask Detector API is running, try enter http://127.0.0.1:4242/api/health in your browser 
 
To see the Face Mask Detector API in action, a simple [Face Mask Detector client](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector/face-mask-detector-client) has been implemented. 

## Requirements:
- [Emily](http://ambolt.io/emily)
