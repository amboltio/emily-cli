
# Face Mask Detector API

The following demonstration shows how to easily get started using a Face Mask Detector, implemented in the Emily API template provided by the [Emily](http://ambolt.io/emily) CLI tool. If you want to learn more about how to implement a Face Mask Detector a detailed and easy to follow guide can be found in the [wiki](https://github.com/amboltio/emily-cli/wiki/Face-mask-detection) 

To run this demo, first download the demo files from this folder, by downloading or cloning the [emily-cli repository](https://github.com/amboltio/emily-cli). 

Make sure you have Emily CLI and its dependencies installed:
1. Download the Emily CLI from [here](http://ambolt.io/emily)
2. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily))
3. Run ```emily doctor``` from your terminal (Bash or PowerShell) to let Emily help you install all dependencies

When all dependencies are installed, open VSCode and from VSCode open the downloaded face-mask-detector-api folder. 

**Attention**: Make sure the face-mask-detector-emily-api folder is opened as a Docker container. If Emily is installed correctly, VSCode will prompt whether it should **"Re-open [the folder] in Container"**. Make sure to press **"OK"** to this.

Finally, start the Face Mask Detector API by executing the following command **from the terminal in VSCode**:
```
python api.py
```

By default, when the API is running it will be accessible at http://127.0.0.1:4242. 
To test if the Face Mask Detector API is running, try entering http://127.0.0.1:4242/api/health in your browser.
 
To see the Face Mask Detector API in action, a simple [Face Mask Detector client](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector/face-mask-detector-client) has been implemented. 
Download and run the client or simply send a POST request to http://127.0.0.1:4242/api/predict with an image attached.
## Requirements:
- [Emily](http://ambolt.io/emily)
