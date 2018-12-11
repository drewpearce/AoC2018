from common import get_inputs_str
from common import log_runtime
from common import now_ms
from statistics import mode
from statistics import StatisticsError


def get_guard_data(inputs):
    inputs = sorted(inputs)
    guards = {}
    id = ''
    sleep = 0
    for item in inputs:
        splits = item.split(' ')
        time = splits[1][3:-1]
        if splits[2] == 'Guard':
            id = splits[3][1:]
        if splits[2] == 'falls':
            sleep = int(time)
        if splits[2] == 'wakes':
            if not guards.get(id):
                guards[id] = [x for x in range(sleep, int(time))]
            else:
                for x in range(sleep, int(time)):
                    guards[id].append(x)

    return guards


def challenge_04_1(inputs):
    guards = get_guard_data(inputs)
    most_sleep = sorted(
        [(k, len(v)) for k, v in guards.items()],
        key=lambda k: k[1],
        reverse=True
    )
    guard = most_sleep[0][0]
    most_common = mode(guards[guard])
    return int(guard) * int(most_common)


def challenge_04_2(inputs):
    guards = get_guard_data(inputs)
    modes = {}
    for k, v in guards.items():
        try:
            this_mode = mode(v)
            modes[k] = this_mode
        except StatisticsError:
            modes[k] = sorted(
                {x: len([y for y in v if y == x]) for x in v},
                key=lambda k: k,
                reverse=True
            )[0]
    mode_counts = sorted(
        [(k, len([x for x in guards[k] if x == v])) for k, v in modes.items()],
        key=lambda k: k[1],
        reverse=True
    )
    guard = mode_counts[0][0]
    minute = modes[guard]
    return int(guard) * int(minute)


inputs = get_inputs_str('day_04.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_04_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_04_2(inputs)))
log_runtime(start_ms)
