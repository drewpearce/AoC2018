from common import get_inputs_str
from common import log_runtime
from common import now_ms
import string


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


inputs = get_inputs_str('day_06.txt')
inputs = [(int(y[0]), int(y[1])) for y in [x.split(', ') for x in inputs]]

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_06_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_06_2(inputs, 10000)))
log_runtime(start_ms)
