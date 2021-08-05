# Face Mask Detector 😷  

[comment]: <> (The following demonstration shows how to easily get started using a Face Mask Detector, implemented in the Emily API template provided by the [Emily]&#40;http://ambolt.io/emily&#41; tool.)

This guide explains how to run an **AI model** which detects whether a person is **wearing a face mask or not** using the Emily CLI. 

<div align="center">
<img src="https://github.com/amboltio/emily-cli/blob/main/tutorials/face-mask-detector/face-mask-detector-client/static/imgs/face_mask_detector.png" alt="Face Mask Detector" width="400" height="500"/>
</div>

## Prerequisites
1. This guide requires that you have [Emily](https://ambolt.io/emily-ai/) installed.
If you haven't installed Emily yet, make sure you [download](https://github.com/amboltio/emily-cli/releases/latest) and [install](https://github.com/amboltio/emily-cli/wiki/Install-Emily) it.  
2. It also requires that you have a **webcam**.

## Start the Face Mask Detector API
1. Start a terminal and run:
```console
$ git clone https://github.com/amboltio/emily-cli.git
$ cd emily-cli/tutorials/face-mask-detector 
$ emily open face-mask-detector-api  # Opens the api in an Emily container
```
2. Select Visual Studio Code as editor  
    * **Note:** After Visual Studio Code is opened you might be asked to rebuild the container and/or reload PyLance - do so.
3. In Visual Studio Code open a terminal and run:
```console
$ python api.py
```
4. You can test that the API is running by navigating to: [http://localhost:4242/api/health](http://localhost:4242/api/health)

## Start the Face Mask Detector Client
1. From the same terminal in which you started the Face Mask Detector API, run:
```console
$ emily open face-mask-detector-client  # Opens the client in an Emily container
```
2. Select Visual Studio Code as editor  
3. In Visual Studio Code open a terminal and run:
```console
$ python main.py
```
4. Open the client at [http://localhost:8000/ ](http://localhost:8000/) to get starting using your face mask detector

<!---
## Learn more: 
Do you want to learn more on how the **Face Mask Detector** is implemented Emily, check out this in-depth walkthrough:
- [Face Maske Detector walkthrough](https://github.com/amboltio/emily-cli/wiki/Face-mask-detection)
- Get information on the [Emily Platform](https://ambolt.io/emily-ai/)
-->
