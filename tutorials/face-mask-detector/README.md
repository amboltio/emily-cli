# Face Mask Detector 😷  

[comment]: <> (The following demonstration shows how to easily get started using a Face Mask Detector, implemented in the Emily API template provided by the [Emily]&#40;http://ambolt.io/emily&#41; tool.)

This guide explains how to run an **AI model** to detect whether a person is **wearing a face mask or not** using the Emily CLI. 

<div align="center">
<img src="https://github.com/amboltio/emily-cli/blob/main/tutorials/face-mask-detector/face-mask-detector-client/static/imgs/face_mask_detector.png" alt="Face Mask Detector" width="400" height="500"/>
</div>

## Prerequisites
This guide requires that you have a **web camera** and [Emily](https://ambolt.io/emily-ai/) installed on your computer.
- Download [Emily](https://github.com/amboltio/emily-cli/releases/latest) for your OS
- Install Emily:
  - [Windows install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily-on-Windows)
  - [Linux install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily-on-Linux)
  - [Mac install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-emily-on-Mac)

## Importing the Project
1. Download the [emily-cli repository files](https://github.com/amboltio/emily-cli).
	* You can either clone or download as a ZIP (remember to unzip)
2. Open a terminal and locate the _/emily-cli/tutorials_ folder
4. Run ```$ emily open ./face-mask-detector/face-mask-detector-api``` to import the Emily project
5. Select a slim image
6. Select the Visual Studio Code editor  
	* **Note:** After Visual Studio Code is opened you might be asked to rebuild the container and/or reload PyLance - do so.

## Running the API
1. Open api.py and press `F5` or press the green _play_ icon in the top right 
	* This will host the API on port _4242_
2. You can check it on [http://localhost:4242/api/health](http://localhost:4242/api/health)

## Interacting with the API

### Importing the client
1. Run ```$ emily open ./face-mask-detector/face-mask-detector-client``` to import the Emily project
2. Select a slim image
3. Select the Visual Studio Code editor  
	* **Note:** After Visual Studio Code is opened you might be asked to rebuild the container and/or reload PyLance - do so.

## Running the client
1. Open main.py and press `F5` or press the green _play_ icon in the top right 
	* This will host the client on port _8888_
2. Open the client at [http://localhost:8000/ ](http://localhost:8000/)

## Learn more: 
Do you want to learn more on how the **Face Mask Detector** is implemented Emily, check out this in-depth walkthrough:
- [Face Maske Detector walkthrough](https://github.com/amboltio/emily-cli/wiki/Face-mask-detection)
- Get information on the [Emily Platform](https://ambolt.io/emily-ai/) 
