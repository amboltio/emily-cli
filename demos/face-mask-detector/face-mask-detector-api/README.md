
# Face Mask Detector API

The following demonstration shows how to easily get started using a Face Mask Detector, implemented in the Emily API template provided by the [Emily](http://ambolt.io/emily) CLI tool. If you want to learn more about how to implement a Face Mask Detector a detailed and easy to follow guide can be found in the [wiki](https://github.com/amboltio/emily-cli/wiki/Face-mask-detection) 

To run this demo, first download the demo files from this folder, by downloading or cloning the [emily-cli repository](https://github.com/amboltio/emily-cli). 

Make sure you have Emily CLI and its dependencies installed:
1. Download the Emily CLI from [here](http://ambolt.io/emily)
2. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily))
3. Run ```emily doctor``` from your terminal (Bash or PowerShell) to let Emily help you install all dependencies
4. `cd` into `face-mask-detector-api/` and run `emily import .`
   - _Some files already exists. Do you want Emily to overwrite them?_
      - Yes
   - _Which Emily image do you want to use?_
      - Full
   - _Do you wish to mount a local drive to the container?_
      - No
   - _Should the project run with GPU and NVIDIA CUDA support?_
      - No need, but you can put "yes" if you want to test your GPU


Then, run `emily open .` to open the project in VS Code.
Once open, start the Face Mask Detector API by executing the following command **from the terminal in VSCode**:

```
python api.py
```

By default, when the API is running on port 4242. It will be accessible at: http://localhost:4242. 
To test if the Face Mask Detector API is running, try entering http://localhost:4242/api/health in your browser.
 
To see the Face Mask Detector API in action, a simple [Face Mask Detector client](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector/face-mask-detector-client) has been implemented. 
Download and run the client or simply send a POST request to http://localhost:4242/api/predict with an image attached.
## Requirements:
- [Emily](http://ambolt.io/emily)
