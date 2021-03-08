
import uvicorn
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from argparse import ArgumentParser

from utilities import get_uptime
from ml.emily import Emily

emily = Emily()

# --- Welcome to your Emily API! --- #
# See the README for guides on how to test it.

# Your API endpoints under http://yourdomain/api/...
# are accessible from any origin by default.
# Make sure to restrict access below to origins you
# trust before deploying your API to production.

parser = ArgumentParser()
parser.add_argument('-e', '--env', default='.env',
                    help='sets the environment file')
args = parser.parse_args()
dotenv_file = args.env
load_dotenv(dotenv_file)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get('HOST_IP')],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/api/health')
def health_check():
    return {
        'uptime': get_uptime(),
        'status': 'UP',
        'port': os.environ.get("HOST_PORT"),
    }


@app.get('/api')
def hello():
    return f'The API is running (uptime: {get_uptime()})'


class TrainItem(BaseModel):
    dataset_path: str
    save_path: str


@app.post('/api/train')
def train(item: TrainItem):
    return {'result': emily.train(item)}


class EvaluateItem(BaseModel):
    dataset_path: str
    model_path: str


@app.post('/api/evaluate')
def evaluate(item: EvaluateItem):
    return {'result': emily.evaluate(item)}


class PredictItem(BaseModel):
    sqft_living: str
    condition: str
    yr_built: str
    model_path: str


@app.post('/api/predict')
def predict(item: PredictItem):
    return {'result': emily.predict(item)}


if __name__ == '__main__':
    host = os.environ.get('HOST_IP')
    if host == '*':
        host = '0.0.0.0'

    uvicorn.run(
        'api:app',
        host=host,
        port=int(os.environ.get('CONTAINER_PORT'))
    )
