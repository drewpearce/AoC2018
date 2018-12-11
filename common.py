import os
import time


def now_ms():
    return int(round(time.time() * 1000))


def log_runtime(start_ms):
    print('Execution took {} ms.'.format(now_ms() - start_ms))


def get_inputs(filename):
    inputs = []
    path = os.path.dirname(__file__) + '/' + filename
    with open(path, 'r') as f:
        for line in f:
            inputs.append(int(line))

    return inputs


def get_inputs_str(filename):
    inputs = []
    path = os.path.dirname(__file__) + '/' + filename
    with open(path, 'r') as f:
        for line in f:
            inputs.append(line.rstrip('\n'))

    return inputs


def get_inputs_single_str(filename):
    path = os.path.dirname(__file__) + '/' + filename
    with open(path, 'r') as f:
        inputs = f.read()

    return inputs
