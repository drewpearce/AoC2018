from funcs import challenge_10_1
from funcs import challenge_10_2
from funcs import get_inputs_str
from funcs import log_runtime
from funcs import now_ms
from test_10 import get_test_inputs


inputs = get_test_inputs()

start_ms = now_ms()
print('Challenge 1 Test results: {}'.format(challenge_10_1(inputs)))
log_runtime(start_ms)
inputs = get_test_inputs()

inputs = get_inputs_str('day_10.txt')
start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_10_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_10_2(inputs)))
log_runtime(start_ms)
