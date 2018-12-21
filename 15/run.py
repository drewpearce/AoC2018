from common import get_inputs_str
from common import log_runtime
from common import now_ms
from day_15 import challenge_15_1
from day_15 import challenge_15_2


inputs = get_inputs_str('day_15.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_15_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_15_2(inputs)))
log_runtime(start_ms)
