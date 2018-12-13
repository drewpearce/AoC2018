from common import get_inputs_str
from common import log_runtime
from common import now_ms
from day_06 import challenge_06_1
from day_06 import challenge_06_2


inputs = get_inputs_str('day_06.txt')
inputs = [(int(y[0]), int(y[1])) for y in [x.split(', ') for x in inputs]]

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_06_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_06_2(inputs, 10000)))
log_runtime(start_ms)
