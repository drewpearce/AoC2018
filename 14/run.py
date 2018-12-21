from common import log_runtime
from common import now_ms
from day_14 import challenge_14_1
from day_14 import challenge_14_2


inputs = '074501'

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_14_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_14_2(inputs)))
log_runtime(start_ms)
