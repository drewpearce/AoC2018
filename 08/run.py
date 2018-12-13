from common import get_inputs_single_str
from common import log_runtime
from common import now_ms
from day_08 import challenge_08_1
from day_08 import challenge_08_2


inputs = get_inputs_single_str('day_08.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_08_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_08_2(inputs)))
log_runtime(start_ms)
