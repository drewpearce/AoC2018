from common import get_inputs_str
from common import log_runtime
from common import now_ms
import re


def get_test_inputs():
    return [
                'position=< 9,  1> velocity=< 0,  2>',
                'position=< 7,  0> velocity=<-1,  0>',
                'position=< 3, -2> velocity=<-1,  1>',
                'position=< 6, 10> velocity=<-2, -1>',
                'position=< 2, -4> velocity=< 2,  2>',
                'position=<-6, 10> velocity=< 2, -2>',
                'position=< 1,  8> velocity=< 1, -1>',
                'position=< 1,  7> velocity=< 1,  0>',
                'position=<-3, 11> velocity=< 1, -2>',
                'position=< 7,  6> velocity=<-1, -1>',
                'position=<-2,  3> velocity=< 1,  0>',
                'position=<-4,  3> velocity=< 2,  0>',
                'position=<10, -3> velocity=<-1,  1>',
                'position=< 5, 11> velocity=< 1, -2>',
                'position=< 4,  7> velocity=< 0, -1>',
                'position=< 8, -2> velocity=< 0,  1>',
                'position=<15,  0> velocity=<-2,  0>',
                'position=< 1,  6> velocity=< 1,  0>',
                'position=< 8,  9> velocity=< 0, -1>',
                'position=< 3,  3> velocity=<-1,  1>',
                'position=< 0,  5> velocity=< 0, -1>',
                'position=<-2,  2> velocity=< 2,  0>',
                'position=< 5, -2> velocity=< 1,  2>',
                'position=< 1,  4> velocity=< 2,  1>',
                'position=<-2,  7> velocity=< 2, -2>',
                'position=< 3,  6> velocity=<-1, -1>',
                'position=< 5,  0> velocity=< 1,  0>',
                'position=<-6,  0> velocity=< 2,  0>',
                'position=< 5,  9> velocity=< 1, -2>',
                'position=<14,  7> velocity=<-2,  0>',
                'position=<-3,  6> velocity=< 2, -1>',
            ]


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


inputs = get_test_inputs()

start_ms = now_ms()
print('Challenge 1 Test results: {}'.format(challenge_10_1(inputs)))
log_runtime(start_ms)
inputs = get_test_inputs()

inputs = get_inputs_str('day_10.txt')
start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_10_1(inputs)))
log_runtime(start_ms)
