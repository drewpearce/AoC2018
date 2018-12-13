from common import get_inputs
from common import get_inputs_str
from common import get_input_single_str
from common import log_runtime
from common import now_ms
from day_13 import challenge_13_1
from day_13 import challenge_13_2


def challenge_13_1(inputs):
    return None


def challenge_13_2(inputs):
    return None


inputs = get_inputs('day_13.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_13_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_13_2(inputs)))
log_runtime(start_ms)
