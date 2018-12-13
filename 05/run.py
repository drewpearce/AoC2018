from common import get_inputs_single_str
from common import log_runtime
from common import now_ms
from day_05 import challenge_05_1
from day_05 import challenge_05_1_redux
from day_05 import challenge_05_2
from day_05 import challenge_05_2_redux


inputs = get_inputs_single_str('day_05.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_05_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_05_2(inputs)))
log_runtime(start_ms)

start_ms = now_ms()
print('Challenge 1 (redux) results: {}'.format(challenge_05_1_redux(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 (redux) results: {}'.format(challenge_05_2_redux(inputs)))
log_runtime(start_ms)
