from funcs import challenge_05_1
from funcs import challenge_05_2
from funcs import get_inputs_single_str
from funcs import log_runtime
from funcs import now_ms


inputs = get_inputs_single_str('day_05.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_05_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_05_2(inputs)))
log_runtime(start_ms)
