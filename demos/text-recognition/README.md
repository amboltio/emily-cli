
# Text Recognition Emily API

This is a demonstration on how to impliment text recognition(also called classification) in the Emily API template provided by the [Emily](http://ambolt.io/emily) CLI tool.  
The accompanying guide can be found in the [Wiki](https://github.com/amboltio/emily-cli/wiki/Text-recognition).

## Setup
To run this demo, download the demo files from this folder, by downloading or cloning the [emily-cli repository](https://github.com/amboltio/emily-cli).

Make sure you have Emily CLI and all the required dependencies installed(everything apart from Nvidia Driver and Nvidia Docker):
1. Download the Emily CLI from [here](http://ambolt.io/emily)
2. Install Emily (see the installation steps [here](https://github.com/amboltio/emily-cli/wiki/How-to-install-Emily))
3. Run ```emily doctor``` from your terminal (Bash or PowerShell) to let Emily help you install all dependencies

**Attention**: Make sure the text-recognition folder is opened as a Docker container. If Emily is installed correctly, VSCode will prompt whether it should **"Re-open [the folder] in Container"**. Make sure to press **"OK"** to this.

## Running API
Start the Text Recogition API by executing the following command **from the terminal in VSCode**:
```
python api.py
```

By default, when the API is running it will be accessible at http://127.0.0.1:4242.
To test the Text Recognition API, try running the following command **from a bash terminal**: 
```
curl http://127.0.0.1:4242/api/health
```
Alternatively the [Postman](https://www.postman.com/) tool can be used. Download and install this software, and then start it. You do not need to register a user in order to use it. Send a GET request to `http://127.0.0.1:4242/api/health`.
This should return:
```
{
  "host": "127.0.0.1",
  "port": 4242,
  "status": "UP",
  "threaded": true,
  "uptime": "0:40:09.718600"
}
```

## Performing training, evaluation and prediction
The repository includes a pre-trained model, hence you can run evaluation or prediction without training a model first. However for continuity, how to send a training request will initially be explained followed by evaluation and lastly prediction.  
**Attention**: The very first time you start the server it may take a while to start. This is because it is downloading lools from the [NLTK toolkit](https://www.nltk.org/).  

### Training
To make a training request to the api a POST request to `http://127.0.0.1:4242/api/train` must be made with the key/value pairs: `dataset_path=emily/data/intents_pizza_chatbot-danish.json` and `save_path=emily/model`. Such a request can be made by running the following command **from a bash terminal**: 
```
curl --location --request POST '127.0.0.1:4242/api/train?dataset_path=emily/data/intents_pizza_chatbot-danish.json&save_path=emily/model'
```
or using [Postman](https://www.postman.com/) sending a POST request to `127.0.0.1:4242/api/train` with the key/value pairs defined in the `Params` field.  

This should return:
```
{
  "success": true
}
```
when the model has finished training.  
You can change the data the model is trained on simply by creating a new `.json` file on the API side and and providing its path as the `dataset_path`. The model can also by saved at a different location by changing the value given to `save_path`. Remember to change `model_path` to the different location as well when performing evaluation and prediction.  
**Attention**: It might take some time if the model and dataset you are using a large as the server will only reply when it is done training.

### Evaluation
To make an evaluation request to the api a POST request to `http://127.0.0.1:4242/api/evaluate` must be made with the key/value pairs: `dataset_path=emily/data/intents_pizza_chatbot-danish.json` and `model_path=emily/model`. Such a request can be made by running the following command **from a bash terminal**: 
```
curl --location --request POST '127.0.0.1:4242/api/evaluate?dataset_path=emily/data/intents_pizza_chatbot-danish.json&model_path=emily/model'
```
or using [Postman](https://www.postman.com/) sending a POST request to `127.0.0.1:4242/api/train` with the key/value pairs defined in the `Params` field.  

This should return:
```
{
  "result": {
    "acc": 1.0,
    "loss": 6.05328350502532e-05
  }
}
```

### Prediction
To make an prediction request to the api a POST request to `http://127.0.0.1:4242/api/predict` must be made with the key/value pairs: `sample=<"some sample">` and `model_path=emily/model`.  
**Attention**: Replace `<"some sample">` with a sample of your choosing. It must be a string without `<>`. For example `sample="Er du der"`.
Such a request can be made by running the following command **from a bash terminal**: 
```
curl --location --request POST '127.0.0.1:4242/api/predict?sample=%22Er%20du%20der%22&model_path=emily/model'
```
**Note**: In the curl request the quotation marks are replaced the `UTF-8` encoding `%22` and spaces are replaced with `%20`.  
Alternativly the request can be made by using [Postman](https://www.postman.com/). Send a POST request to `127.0.0.1:4242/api/predict` with the key/value pairs defined in the `Params` field.  
**Note**: When using Postman the sample does not need to be manually encoded - simply write the sample in the value field. Remember to include quotation marks! 
This should return:
```
{
  "prediction": {
    "class": "prompt-for-presence",
    "prob": 0.9999352693557739
  }
}
```

## Requirements:
- [Emily](http://ambolt.io/emily)


