# Face Mask Detector Client:

The purpose of this client is to test the [Face Mask Detector API](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector/face-mask-detector-emily-api).

The Face Mask Detector client makes use of your web camera and sends POST requests to the Face Mask Detector API.

Before running the client make sure the Face Mask Detector API is up and running at http://127.0.0.1:4242. See [Face Mask Detector Emily API](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector/face-mask-detector-emily-api) for how to start the API. 

If the Face Mask Detector API is already running, start the client, by executing:
```
python main.py
```
from inside the face-mask-detector-client folder. This will start serving the index.html file on port 8000.
 
Alternatively, any other http serving tool can be used.

## Requirements:
- A web camera
- Python
