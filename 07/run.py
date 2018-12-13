from common import get_inputs_str
from common import log_runtime
from common import now_ms
from day_07 import challenge_07_1
from day_07 import challenge_07_2


inputs = get_inputs_str('day_07.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_07_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_07_2(inputs, 5, 60)))
log_runtime(start_ms)
