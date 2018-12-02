from funcs import challenge_02_1
from funcs import challenge_02_2
from funcs import get_inputs_str
from funcs import log_runtime
from funcs import now_ms


inputs = get_inputs_str('day_02.txt')
start_ms = now_ms()
print('Challenge 1 result: {}'.format(challenge_02_1(inputs)))
log_runtime(start_ms)
start_ms = now_ms()
print('Challenge 2 result: {}'.format(challenge_02_2(inputs)))
log_runtime(start_ms)
