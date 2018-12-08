from funcs import challenge_08_1
from funcs import challenge_08_2
from funcs import get_inputs_single_str
from funcs import log_runtime
from funcs import now_ms
import os

in_file = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'day_08.txt'
)
inputs = get_inputs_single_str(in_file)

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_08_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_08_2(inputs)))
log_runtime(start_ms)
