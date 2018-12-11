from common import get_inputs
from common import get_inputs_str
from common import get_input_single_str
from common import log_runtime
from common import now_ms


def challenge_11_1(inputs):
    return None


def challenge_11_2(inputs):
    return None


inputs = get_inputs('day_11.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_11_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_11_2(inputs)))
log_runtime(start_ms)
