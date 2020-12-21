
from flask import request, jsonify
import json
from utilities import get_uptime, configure_app
from ml.emily import Emily
from waitress import serve

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


@app.route('/api/health')
def healthcheck():
    return jsonify({
        'uptime': get_uptime(),
        'status': 'UP',
        'host': config['connection']['host'],
        'port': config['connection']['port'],
    })


@app.route('/api')
def hello():
    return f'The {config["project_name"]} API is running (uptime: {get_uptime()})'


@app.route('/api/train', methods=['POST'])
def train():
    return jsonify({
        'result': emily.train(request)
    })


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Expected request fields:
    sample
    """
    return jsonify({
        'result': emily.predict(request)
    })


if __name__ == '__main__':
    # Train the model when the API starts (training is skipped after the data has been written once)
    emily.trainer.train(request)
    serve(
        app, listen=f'{config["connection"]["host"]}:{config["connection"]["port"]}')
