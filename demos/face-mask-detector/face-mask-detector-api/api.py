import json
import os

from flask import request, jsonify
from waitress import serve

from utilities import get_uptime, configure_app
from ml.emily import Emily

emily = Emily()

# --- Welcome to your Emily API! --- #

# See the README for guides on how to test it.

# Your API endpoints under http://yourdomain/api/...
# are accessible from any origin by default.
# Make sure to restrict access below to origins you
# trust before deploying your API to production.

config_file = 'config.json'
config = json.load(open(config_file))

app = configure_app(config['project_name'], cors={
    r'/api/*': {
        "origins": "*"
    }
})


@app.route('/api/predict', methods=['POST'])
def predict():

    sample = request.form['sample']
    model_path = os.path.join(os.getcwd(), "data/custom_model.pt")

    return jsonify({
        'prediction': emily.predict(sample, model_path)
    })


@app.route('/api/train', methods=['POST'])
def train():

    dataset_path = request.args['dataset_path']
    save_path = request.args['save_path']

    return jsonify({
        'success': emily.train(dataset_path, save_path)
    })


@app.route('/api/evaluate', methods=['POST'])
def evaluate():

    dataset_path = request.args['dataset_path']
    model_path = request.args['model_path']

    return jsonify({
        'result': emily.evaluate(dataset_path, model_path)
    })


@app.route('/api')
def hello():
    return f'The {config["project_name"]} API is running (uptime: {get_uptime()})'


@app.route('/api/health')
def healthcheck():
    return jsonify({
        'uptime': get_uptime(),
        'status': 'UP',
        'host': config['connection']['host'],
        'port': config['connection']['port'],
        'threaded': config['connection']['threaded']
    })


if __name__ == '__main__':
    serve(app, listen=f'{config["connection"]["host"]}:{config["connection"]["port"]}')
