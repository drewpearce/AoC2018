from common import get_inputs_str
from common import log_runtime
from common import now_ms
from day_03 import challenge_03_1
from day_03 import challenge_03_2


inputs = get_inputs_str('day_03.txt')

start_ms = now_ms()
print('Challenge 1 result: {}'.format(challenge_03_1(inputs)))
log_runtime(start_ms)

start_ms = now_ms()
print('Challenge 2 result: {}'.format(challenge_03_2(inputs)))
log_runtime(start_ms)