

import uvicorn
import os
import traceback

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from argparse import ArgumentParser

from src.trainer import Trainer
from src.evaluator import Evaluator
from src.predictor import Predictor
from src.requests import PredictRequest, PredictWebcamRequest, TrainRequest, EvaluateRequest

# --- Welcome to your Emily API! --- #
# See the README for guides on how to test it.

# Your API endpoints under http://yourdomain/api/...
# are accessible from any origin by default.
# Make sure to restrict access below to origins you
# trust before deploying your API to production.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Below you find your API's Endpoints ---
@app.get('/api/health')
def health_check():
    return {
        'status': 'UP',
        'port': os.environ.get("HOST_PORT"),
    }


@app.post('/api/train')
def train(request_item: TrainRequest):

    try:
        # Initialize Trainer object
        trainer = Trainer(request_item)

        accuracy, model_name = trainer.train()

        return {
            'status': "Training is complete",
            'best accuracy': accuracy,
            'model': model_name
        }

    except Exception as err:
        return {
            'status': str(err),
            'stack_trace': str(traceback.format_exc())
        }


@app.post('/api/evaluate')
def evaluate(request_item: EvaluateRequest):

    try:
        # Initialize Evaluator object
        evaluator = Evaluator(request_item)

        # Start evaluation
        accuracy = evaluator.evaluate()

        return {
            'status': "Evaluation is complete!",
            'accuracy': accuracy,
        }

    except Exception as err:
        return {
            'status': str(err),
            'stack_trace': str(traceback.format_exc())
        }


@app.post('/api/predict')
def predict_v1(request_item: PredictRequest):

    try:
        # Initialize predictor object

        predictor = Predictor(request_item.model_path)

        # Start prediction
        prediction = predictor.predict(request_item.img_path)

        print(prediction)

        return {
            'status': 'Prediction is complete!',
            'prediction': prediction
        }

    except Exception as err:
        return {
            'status': str(err),
            'stack_trace': str(traceback.format_exc())
        }


@app.post('/api/predict-webcam')
def predict_webcam(request_item: PredictWebcamRequest):

    print(request_item.model_path)
    print(type(request_item.image))

    try:
        # Initialize predictor object
        predictor = Predictor(request_item.model_path)

        # Start prediction
        prediction = predictor.predict_webcam(request_item.image)

        return {
            'status': 'Prediction is complete!',
            'prediction': prediction
        }

    except Exception as err:
        return {
            'status': str(err),
            'stack_trace': str(traceback.format_exc())
        }


# Load environment variables from the projects env file
parser = ArgumentParser()
parser.add_argument('-e', '--env', default='.env',
                    help='sets the environment file')
args = parser.parse_args()
dotenv_file = args.env
load_dotenv(dotenv_file)

if __name__ == '__main__':

    # Start the uvicorn server
    uvicorn.run(
        'api:app',
        host=os.environ.get('HOST_IP'),
        port=int(os.environ.get('CONTAINER_PORT'))
    )
