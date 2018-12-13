from common import get_inputs_str
from common import log_runtime
from common import now_ms
from day_12 import challenge_12_1
from day_12 import challenge_12_2


inputs = get_inputs_str('day_12.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_12_1(inputs, 20)))
log_runtime(start_ms)

start_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_12_2(inputs, 50000000000)))
log_runtime(start_ms)
