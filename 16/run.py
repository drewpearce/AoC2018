from common import get_inputs_str
from common import log_runtime
from common import now_ms
from day_16 import challenge_16_1
from day_16 import challenge_16_2


inputs = get_inputs_str('day_16.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_16_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_16_2(inputs)))
log_runtime(start_ms)
