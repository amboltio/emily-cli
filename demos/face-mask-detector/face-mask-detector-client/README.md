# Face Mask Detector Client:

The purpose of this client is to test the [Face Mask Detector API](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector/face-mask-detector-api).

The Face Mask Detector client makes use of your web camera and sends POST requests to the Face Mask Detector API.

Before running the client make sure the Face Mask Detector API is up and running on port 4242 (http://localhost:4242). See [start the Face Mask Detector Emily API](https://github.com/amboltio/emily-cli/tree/main/demos/face-mask-detector/face-mask-detector-api).

If the Face Mask Detector API is already running, start the client, by executing:
```
python main.py
```
from inside the face-mask-detector-client folder. This will start serving the index.html file on port 8000.
 
Alternatively, any other http serving tool can be used.

Finally, open the served client here: http://localhost:8000/

## Requirements:
- A web camera
- Python
