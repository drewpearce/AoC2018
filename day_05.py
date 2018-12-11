from common import get_inputs_single_str
from common import log_runtime
from common import now_ms
import re
import string


def generate_regex(join=True):
    doubles = []
    for ltr in string.ascii_lowercase:
        doubles.append(ltr + ltr.upper())
        doubles.append(ltr.upper() + ltr)

    if not join:
        return doubles

    return '|'.join(doubles)


def challenge_05_1(inputs):
    reg = generate_regex()
    matches = True
    while matches:
        match = re.subn(reg, '', inputs)
        if match[0] != inputs:
            inputs = match[0]
        else:
            matches = False
    return len(inputs)


def challenge_05_1_redux(inputs):
    keys = {x: x.upper() for x in string.ascii_lowercase}
    keys.update({x: x.lower() for x in string.ascii_uppercase})
    pos = 0
    data = [x for x in inputs]

    while pos < len(data) - 1:
        while pos < len(data) - 1:
            c = data[pos]
            n = data[pos + 1]
            if keys[c] == n:
                data.pop(pos)
                data.pop(pos)
                pos -= 1
                break
            pos += 1

    return len(data)


def challenge_05_2(inputs):
    results = []
    for ltr in string.ascii_lowercase:
        if ltr in inputs or ltr.upper() in inputs:
            repl = inputs.replace(ltr, '')
            repl = repl.replace(ltr.upper(), '')
            results.append(challenge_05_1(repl))

    return sorted(results)[0]


def challenge_05_2_redux(inputs):
    results = []
    for ltr in string.ascii_lowercase:
        if ltr in inputs or ltr.upper() in inputs:
            repl = inputs.replace(ltr, '')
            repl = repl.replace(ltr.upper(), '')
            results.append(challenge_05_1_redux(repl))

    return sorted(results)[0]


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
