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
