from common import get_inputs
from common import log_runtime
from common import now_ms
from day_01 import challenge_01_1
from day_01 import challenge_01_2_redux


inputs = get_inputs('day_01.txt')

start_ms = now_ms()
print('Challenge 1 result: {}'.format(challenge_01_1(inputs)))
log_runtime(start_ms)

start_ms = now_ms()
print('Challenge 2 result: {}'.format(challenge_01_2_redux(inputs)))
log_runtime(start_ms)