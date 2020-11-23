# Sentiment Analysis demo

This demo contains an Emily microservice for conducting sentiment analysis, and a web client that consumes the API exposed by the microservice. 

## Guide

See the [guide](https://github.com/amboltio/emily-cli/wiki/Sentiment-analysis) for a full walkthrough of the implementation.

## Quick start

**Start the API**
Run the following commands to launch the API: 
```
cd sentiment-analysis-api
code .
```

When Visual Studio Code opens up, click "Reopen in Container" when prompted.
Once VS Code has opened inside the the Docker container, run `python api.py` from the VS Code terminal. 

**Start the client**: 
```
cd client
python3 -m http.server 8000
```

... or start any other HTTP server that serves `client/index.html`. 
Open `http://localhost:8000` in your browser.
