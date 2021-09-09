# Face Mask Detector  

[comment]: <> (The following demonstration shows how to easily get started using a Face Mask Detector, implemented in the Emily API template provided by the [Emily]&#40;http://ambolt.io/emily&#41; tool.)

This guide explains how to run an **AI model** which can detect whether a person is **wearing a face mask or not** using the Emily CLI. 

<div align="center">
<img src="https://github.com/amboltio/emily-cli/blob/main/tutorials/face-mask-detector/face-mask-detector-client/static/imgs/face_mask_detector.png" alt="Face Mask Detector" width="400" height="500"/>
</div>

## Before you start
This guide requires that you have a **web camera** and [Emily](https://ambolt.io/emily-ai/) installed on your computer.
- Download [Emily](https://github.com/amboltio/emily-cli/releases/latest) for your OS
- Install Emily:
  - [Windows install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily-on-Windows)
  - [Linux install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily-on-Linux)
  - [Mac install guide](https://github.com/amboltio/emily-cli/wiki/How-to-install-emily-on-Mac)



## Start the Face Mask Detector API
```console
$ git clone https://github.com/amboltio/emily-cli.git
$ cd emily-cli/tutorials/face-mask-detector 
$ emily open face-mask-detector-api  # Open the api running on port 4242
```

- **OPS**: Open the face-mask-detector-api in **Visual Studio Code**.
- In Visual Studio Code open a terminal and run:
```console
$ python api.py
```

The face-mask-detector-api should now be hosting a FastAPI api on port 4242!

## Start the Face Mask Detector Client
```console
$ emily open face-mask-detector-client  # Open the client 
```
- **OPS**: Open the face-mask-detector-client in **Visual Studio Code**.
- In Visual Studio Code open a terminal and run:
```console
$ python main.py
```
## Finally:
Your Face Mask detector client is now running in your browser.
- Go to http://localhost:8000/ (It might take a few seconds before the client is running)



## Learn more: 

Do you want to learn more on how the **Face Mask Detector** is implemented Emily, check out this in-depth walkthrough:

- [Face Maske Detector walkthrough](https://github.com/amboltio/emily-cli/wiki/Face-mask-detection)
- For more information on the [Emily Platform](https://ambolt.io/emily-ai/) 
