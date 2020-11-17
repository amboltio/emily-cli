# Linear Regression API
This demo shows how to easily implement a linear regression in the Emily API template provided by the [Emily](http://ambolt.io/emily) CLI tool.
The accompanying guide can be found at [https://github.com/amboltio/emily-cli/wiki/Linear-regression](https://github.com/amboltio/emily-cli/wiki/Linear-regression).

To run this demo, first download the demo files from this folder, by downloading or cloning the [emily-cli repository](https://github.com/amboltio/emily-cli). 

Make sure you have Emily CLI and its dependencies installed:
1. Download the Emily CLI from [here](http://ambolt.io/emily)
2. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily))
3. Run ```emily doctor``` from your terminal (Bash or PowerShell) to let Emily help you install all dependencies

When all dependencies are installed, open VSCode and from VSCode open the downloaded linear-regression folder. 

**Attention**: Make sure the linear-regression folder is opened as a Docker container. If Emily is installed correctly, VSCode will prompt whether it should **"Re-open [the folder] in Container"**. Make sure to press **"OK"** to this.

Finally, start the Linear Regression API by executing the following command **from the terminal in VSCode**:
```
python api.py
```

By default, when the API is running it will be accessible at http://127.0.0.1:4242.
To test if the Face Mask Detector API is running, try entering http://127.0.0.1:4242/api/health in your browser.
Training, evaluating, and predicting using the model is done by sending POST requests to the train, evaluate, and predict endpoints, respectively.

## Requirements:
- [Emily](http://ambolt.io/emily)
