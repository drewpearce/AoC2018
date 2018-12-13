from common import get_inputs_single_str


def calculate_cell_power(pos):
    rack_id = pos[0] + 10
    power = rack_id * pos[1]
    power += SERIAL
    power *= (pos[0] + 10)
    power = int(power / 100)
    power = power % 10
    power -= 5
    return power


GRID = 300
SERIAL = int(get_inputs_single_str('day_11.txt'))
CELLS = {
    (x, y): calculate_cell_power((x, y))
    for x in range(1, GRID + 1)
    for y in range(1, GRID + 1)
}


def get_cell_power_block(pos, size=3):
    return sum(
        [CELLS[(x, y)]
         for x in range(pos[0], pos[0] + size)
         for y in range(pos[1], pos[1] + size)]
    )


def challenge_11_1(size=3):
    vals = {
        (x, y): get_cell_power_block((x, y), size)
        for x in range(1, GRID - size + 1)
        for y in range(1, GRID - size + 1)
    }
    largest = max(vals, key=lambda k: vals[k])
    return largest, vals[largest]


def challenge_11_2():
    vals = []
    down_count = 0
    for size in range(1, 300):
        val = challenge_11_1(size)
        if not vals or val[1] > vals[-1][1]:
            vals.append(((val[0][0], val[0][1], size), val[1]))
            down_count = 0
        else:
            vals.append(((val[0][0], val[0][1], size), val[1]))
            down_count += 1
            if down_count == 5:
                return vals[-6]
