from collections import defaultdict
from collections import deque
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
        except Exception:
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
                x: {sum(1 for z in range(0, len(x)) if x[z] != y[z]): y
                    for y in set(inputs)
                    if sum(1 for z in range(0, len(x)) if x[z] != y[z]) == 1}
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

    areas = [{'label': k, 'area': len(
             [x for x, v in all_coords.items() if v == k])}
             for k in locs.keys() if k not in infinites]

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


def parse_challenge_07_inputs(inputs):
    order_rules = []
    for rule in inputs:
        f = rule.split(' ')[1]
        l = rule.split('step ')[1][0]
        order_rules.append(
            {
                'f': f,
                'l': l
            }
        )

    return order_rules


def challenge_07_1(inputs):
    rules = parse_challenge_07_inputs(inputs)
    all_used_ltrs = set([r['f'] for r in rules] + [r['l'] for r in rules])
    afters = {l: sorted([x['f'] for x in rules if x['l'] == l])
              for l in all_used_ltrs}
    out = ''
    while len(out) < len(all_used_ltrs):
        possible = sorted(
            [k for k, v in afters.items() if v == [] and k not in out]
        )
        out += possible[0]
        for k, v in afters.items():
            if possible[0] in v:
                afters[k].remove(possible[0])
    return out


def challenge_07_2(inputs, workers, time_mod):
    times = {v: i + 1 + time_mod for i, v in enumerate(string.ascii_uppercase)}
    rules = parse_challenge_07_inputs(inputs)
    all_used_ltrs = set([r['f'] for r in rules] + [r['l'] for r in rules])
    afters = {l: sorted([x['f'] for x in rules if x['l'] == l])
              for l in all_used_ltrs}
    out = []
    workers = {
        x: {'start': None, 'end': None, 'working': False, 'ltr': 0}
        for x in range(0, workers)
    }
    time = 0
    while len(all_used_ltrs) > 0:
        for w in workers:
            if workers[w]['working'] is True:
                if workers[w]['end'] == time:
                    for k, v in afters.items():
                        if workers[w]['ltr'] in v:
                            afters[k].remove(workers[w]['ltr'])
                    workers[w]['working'] = False
                    all_used_ltrs.remove(workers[w]['ltr'])
        possible = sorted(
            [k for k, v in afters.items() if v == [] and k not in out]
        )
        for x in possible:
            avail = [k for k, v in workers.items() if v['working'] is False]
            if avail:
                wkr = avail[0]
                workers[wkr]['start'] = time
                workers[wkr]['end'] = time + times[x]
                workers[wkr]['working'] = True
                workers[wkr]['ltr'] = x
                out.append(x)
        time += 1
    return time - 1


def challenge_08_get_nodes(inputs):
    def concat_x(val, count):
        x = val
        for _ in range(count):
            x += val
        return x

    # parse the inputs.
    inputs = [int(x) for x in inputs.split(' ')]
    nodes = []
    names = [x for x in string.ascii_uppercase]
    get_child = (False, None)
    complete_parent = False

    # loop through inputs and build the nodes object
    while inputs:
        if not names:
            count = len([x['name'] for x in nodes][-1])
            names = [concat_x(x, count) for x in string.ascii_uppercase]

        parent = get_child[1]
        if not complete_parent:
            name = names.pop(0)
            child_count = inputs.pop(0)
            meta_count = inputs.pop(0)
            if child_count == 0:
                children = None
                meta = [x for x in inputs[0: meta_count]]
                for _ in range(meta_count):
                    inputs.pop(0)
            else:
                children = []
                meta = []
                get_child = (True, name)

            nodes.append(
                {
                    'name': name,
                    'child_count': child_count,
                    'meta_count': meta_count,
                    'children': children,
                    'meta': meta,
                    'parent': parent
                }
            )

        else:
            node_id = [i for i, x in enumerate(nodes)
                       if x['name'] == parent][0]
            meta_count = nodes[node_id]['meta_count']
            meta = [x for x in inputs[0: meta_count]]
            for _ in range(meta_count):
                inputs.pop(0)
            nodes[node_id]['meta'] = meta
            parent = nodes[node_id]['parent']
            child_count = 0

        if parent:
            parent_id = [i for i, x in enumerate(nodes)
                         if x['name'] == parent][0]
            if not complete_parent:
                nodes[parent_id]['children'].append(name)
            if nodes[parent_id]['child_count'] == len(
                    nodes[parent_id]['children']) and child_count == 0:
                get_child = (False, parent)
                complete_parent = True
            elif child_count == 0:
                get_child = (True, parent)
                complete_parent = False
        else:
            complete_parent = False

    return nodes


def challenge_08_1(inputs):
    nodes = challenge_08_get_nodes(inputs)
    meta_sum = sum([sum(x['meta']) for x in nodes])
    return meta_sum


def challenge_08_2(inputs):
    nodes = challenge_08_get_nodes(inputs)

    def calcultate_node_values(node):
        id = [i for i, x in enumerate(nodes) if x['name'] == node][0]
        if nodes[id]['child_count'] == 0:
            return sum(nodes[id]['meta'])
        else:
            children = [0]
            for i in nodes[id]['meta']:
                if i > 0 and i <= nodes[id]['child_count']:
                    children.append(
                        calcultate_node_values(nodes[id]['children'][i - 1])
                    )
            return sum(children)
    root_val = calcultate_node_values('A')
    return root_val


def play_marble_game(players, marble_max):
    board = deque([0])
    scores = defaultdict(int)
    for marble in range(1, marble_max + 1):
        current_player = marble % players

        if marble % 23 == 0:
            board.rotate(7)
            scores[current_player] += marble + board.pop()
            board.rotate(-1)
        else:
            board.rotate(-1)
            board.append(marble)

    return sorted([v for k, v in scores.items()], reverse=True)[0]


def challenge_09_1(inputs):
    players = int(inputs.split(' ')[0])
    marble_max = int(inputs.split(' ')[-2])
    return play_marble_game(players, marble_max)


def challenge_09_2(inputs):
    players = int(inputs.split(' ')[0])
    marble_max = int(inputs.split(' ')[-2]) * 100
    return play_marble_game(players, marble_max)


def challenge_10_parse_inputs(inputs):
    # parse the text input into usable coordinates
    coords = []
    reg = re.compile('([-]*[0-9]+)')
    for line in inputs:
        matches = re.findall(reg, line)
        if matches:
            x = int(matches[0])
            y = int(matches[1])
            v_x = int(matches[2])
            v_y = int(matches[3])
            coords.append({
                'x': x,
                'y': y,
                'v_x': v_x,
                'v_y': v_y
            })

    return coords


def challenge_10_iterate_coords(coords, i=1):
    # return new coordinates based on i iterations
    return [
        {
            'x': c['x'] + (i * c['v_x']),
            'y': c['y'] + (i * c['v_y']),
            'v_x': c['v_x'],
            'v_y': c['v_y']
        }
        for c in coords
    ]


def challenge_10_1(inputs):
    coords = challenge_10_parse_inputs(inputs)
    x_range = max([c['x'] for c in coords]) - min([c['x'] for c in coords])
    y_range = max([c['y'] for c in coords]) - min([c['y'] for c in coords])
    ranges = [(x_range, y_range)]
    test = [c for c in coords]
    i = 0
    while True:
        test = challenge_10_iterate_coords(test)
        x_range = max([c['x'] for c in test]) - min([c['x'] for c in test])
        y_range = max([c['y'] for c in test]) - min([c['y'] for c in test])
        if x_range > ranges[i][0] and y_range > ranges[i][1]:
            temp = challenge_10_iterate_coords(coords, i)
            ch10_print_coords(temp)
            print(i)
            break
        else:
            ranges.append((x_range, y_range))
            i += 1

    return None


def ch10_print_coords(coords, iterator=None):
    # print the coordinates on the terminal
    xs = [c['x'] for c in coords]
    xmax = max(xs)
    if iterator is None:
        iterator = xmax + 1
    total_max = xmax
    counter = 0
    while counter < total_max:
        temp = [c for c in coords
                if c['x'] < counter + iterator
                and c['x'] >= counter]
        xs = [c['x'] for c in temp]
        xmax = max(xs)
        xmin = min(xs)
        # was sorting this reverse (highest to lowest) but then remembered in
        # problem that the y values are backwards from what you would normally
        # expect (+ is down, - is up)
        ys = sorted([c['y'] for c in coords])
        lines = []
        for y in ys:
            lines.append({y: [c['x'] for c in temp if c['y'] == y]})

        for i, line in enumerate(lines):
            if (i + 5) % 5 == 0:
                pline = ''
                for x in range(xmin, xmax + 1):
                    k = list(line)[0]
                    if x in line[k]:
                        pline += ' # '
                    else:
                        pline += '   '
                print(pline)

        counter += iterator
