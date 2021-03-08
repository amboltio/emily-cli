
import datetime
import time
import json
import numpy as np

START_TIME = time.time()

def get_uptime(start_time=START_TIME):
    return '{}'.format(datetime.timedelta(seconds=time.time() - start_time))


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)
