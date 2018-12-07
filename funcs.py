import os
import re
from statistics import mode
from statistics import StatisticsError
import string
import time


def now_ms():
    return int(round(time.time() * 1000))


def log_runtime(start_ms):
    print('Execution took {} ms.'.format(now_ms() - start_ms))


def get_inputs(filename):
    inputs = []
    path = os.path.dirname(__file__) + '/' + filename
    with open(path, 'r') as f:
        for line in f:
            inputs.append(int(line))

    return inputs


def get_inputs_str(filename):
    inputs = []
    path = os.path.dirname(__file__) + '/' + filename
    with open(path, 'r') as f:
        for line in f:
            inputs.append(line.rstrip('\n'))

    return inputs


def get_inputs_single_str(filename):
    with open(filename, 'r') as f:
        inputs = f.read()

    return inputs


def challenge_01_1(inputs):
    return sum(inputs)


def challenge_01_2(inputs):
    dupe = False
    sums = [0]
    inc = 0
    while dupe is False:
        freq = sums[-1] + inputs[inc]
        inc += 1
        if freq in sums:
            dupe = freq
            return freq
        else:
            sums.append(freq)

        if inc >= len(inputs):
            inc = 0


def challenge_01_2_redux(inputs):
    copy = [x for x in inputs]
    sums = set([0])
    current_sum = 0

    while True:
        try:
            current_sum += copy.pop(0)
        except:
            copy = [x for x in inputs]
            current_sum += copy.pop(0)

        if current_sum in sums:
            return current_sum
        else:
            sums.add(current_sum)


def challenge_02_1(inputs):
    sets = {'2': 0, '3': 0}
    for label in inputs:
        temp = {}
        for char in label:
            if temp.get(char):
                temp[char] += 1
            else:
                temp[char] = 1
        vals = set([v for k, v in temp.items()])
        if 2 in vals:
            sets['2'] += 1
        if 3 in vals:
            sets['3'] += 1
    return sets['2'] * sets['3']


def challenge_02_2(inputs):
    labels = {}
    for x in set(inputs):
        labels.update(
            {
                x: {sum(1 for z in range(0, len(x)) if x[z] != y[z]): y for y in set(inputs) if sum(1 for z in range(0, len(x)) if x[z] != y[z]) == 1}
            }
        )

    labels = {x for x, val in labels.items() if 1 in val.keys()}
    if len(labels) == 2:
        return''.join([x for x in list(labels)[0] if x in list(labels)[1]])
    else:
        return None


def load_claim(text):
    chunks = text.split(' ')
    loc = chunks[2][0:-1]
    size = chunks[3]
    return {
        'claim': int(chunks[0][1:]),
        'x': int(loc.split(',')[0]),
        'y': int(loc.split(',')[1]),
        'w': int(size.split('x')[0]),
        'h': int(size.split('x')[1])
    }


def challenge_03_1(inputs):
    grid = {}
    for x in inputs:
        data = load_claim(x)
        for h in range(0, data['h']):
            for w in range(0, data['w']):
                loc_x = data['x'] + w
                loc_y = data['y'] + h
                key = str(loc_x) + ',' + str(loc_y)
                if not grid.get(key):
                    grid[key] = 1
                else:
                    grid[key] += 1
    grid = {k: v for k, v in grid.items() if v >= 2}
    return len(grid)


def challenge_03_2(inputs):
    grid = {}
    for x in inputs:
        data = load_claim(x)
        for h in range(0, data['h']):
            for w in range(0, data['w']):
                loc_x = data['x'] + w
                loc_y = data['y'] + h
                key = str(loc_x) + ',' + str(loc_y)
                if not grid.get(key):
                    grid[key] = [data['claim']]
                else:
                    grid[key].append(data['claim'])
    grid1 = set([v[0] for k, v in grid.items() if len(v) == 1])
    grid2 = []
    for k, v in grid.items():
        if len(v) > 1:
            for x in v:
                grid2.append(x)
    grid2 = set(grid2)
    return([x for x in grid1 if x not in grid2][0])


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


def get_manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def get_max_grid(inputs):
    max_grid = sorted([
        sorted([x[0] for x in inputs], reverse=True)[0],
        sorted([x[1] for x in inputs], reverse=True)[0]
    ])
    max_grid = max_grid[1]
    return max_grid


def challenge_06_1(inputs):
    labels = [x for x in string.ascii_letters]
    locs = {labels.pop(0): x for x in inputs}
    max_grid = get_max_grid(inputs)
    all_coords = {}
    for x in range(0, max_grid + 1):
        all_coords.update({(x, y): None for y in range(0, max_grid + 1)})

    for coord in all_coords:
        distances = sorted(
            [{'label': k, 'distance': get_manhattan_distance(v, coord)}
             for k, v in locs.items()],
            key=lambda k: k['distance']
        )
        if distances[0]['distance'] == distances[1]['distance']:
            all_coords[coord] = '_'
        else:
            all_coords[coord] = distances[0]['label']

    infinites = set([v for k, v 
                    in all_coords.items()
                    if k[0] == max_grid
                    or k[1] == max_grid
                    or k[0] == 0
                    or k[1] == 0])

    areas = [{'label': k, 'area': len([x for x, v in all_coords.items() if v == k])} for k in locs.keys() if k not in infinites]

    return sorted(areas, key=lambda k: k['area'], reverse=True)[0]['area']


def challenge_06_2(inputs, max_distance):
    max_grid = get_max_grid(inputs)
    all_coords = []
    for x in range(0, max_grid + 1):
        for y in range(0, max_grid + 1):
            all_coords.append((x, y))

    matches = [
        loc for loc in all_coords
        if sum([get_manhattan_distance(loc, x) for x in inputs]) < max_distance
    ]

    return len(matches)


def challenge_07_1(inputs):
    return None


def challenge_07_2(inputs):
    return None
