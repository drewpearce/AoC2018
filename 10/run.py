from common import get_inputs_str
from common import log_runtime
from common import now_ms
from day_10 import challenge_10_1
from day_10 import get_test_inputs


inputs = get_test_inputs()

start_ms = now_ms()
print('Challenge 1 Test results: {}'.format(challenge_10_1(inputs)))
log_runtime(start_ms)
inputs = get_test_inputs()

inputs = get_inputs_str('day_10.txt')
start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_10_1(inputs)))
log_runtime(start_ms)
