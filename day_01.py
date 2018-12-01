from funcs import challenge_01_1
from funcs import challenge_01_2_redux
from funcs import get_inputs
from funcs import log_runtime
from funcs import now_ms


inputs = get_inputs('day_01.txt')
start_ms = now_ms()
print('Challenge 1 result: {}'.format(challenge_01_1(inputs)))
log_runtime(start_ms)
start_ms = now_ms()
print('Challenge 2 result: {}'.format(challenge_01_2_redux(inputs)))
log_runtime(start_ms)
