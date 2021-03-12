
import uvicorn
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from argparse import ArgumentParser

from utilities import get_uptime
from ml.trainer import Trainer
from ml.evaluator import Evaluator


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
    allow_origins=["*"],
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


class TrainItem(BaseModel):
    train_csv: str
    val_csv: str
    batch_size: int
    learning_rate: float
    epochs: int
    train_seed: int
    save_path: str


@app.post('/api/train')
def train(request_item: TrainItem):
    trainer = Trainer(
        train_csv=request_item.train_csv,
        val_csv=request_item.val_csv,
        batch_size=request_item.batch_size,
        learning_rate=request_item.learning_rate,
        epochs=request_item.epochs,
        seed=request_item.train_seed,
        save_path=request_item.save_path
    )

    model, train_losses, val_losses, train_accs, val_accs = trainer.train()
    return {'status': "done"}


class EvaluateItem(BaseModel):
    model_path: str
    test_csv: str
    batch_size: int


@app.post('/api/evaluate')
def evaluate(request_item: EvaluateItem):
    try:
        # Init evaluator object
        evaluator = Evaluator(request_item.model_path,
                              request_item.test_csv,
                              request_item.batch_size)
        test_acc, tps, fps, tns, fns = evaluator.evaluate()
        return {
            'samples': sum([tps, fps, tns, fns]),
            'positives': tps + fns,
            'negatives': tns + fps,
            'tps': tps,
            'fps': fps,
            'tns': tns,
            'fns': fns,
            'acc': f'{test_acc}%'
        }
    except Exception as err:
        return {
            'error': str(err)
        }


class PredictItem(BaseModel):
    sample: str
    model_path: str


@app.post('/api/predict')
def predict(item: PredictItem):
    return {'result': "none"}


if __name__ == '__main__':

    uvicorn.run(
        'api:app',
        host=os.environ.get('HOST_IP'),
        port=int(os.environ.get('CONTAINER_PORT'))
    )

