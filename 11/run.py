from common import log_runtime
from common import now_ms
from day_11 import challenge_11_1
from day_11 import challenge_11_2

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_11_1()))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_11_2()))
log_runtime(start_ms)
