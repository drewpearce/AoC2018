import heapq


class Unit(object):
    def __init__(self, pos, unit_type):
        self.pos = pos
        self.hp = 200
        self.alive = True
        self.type = unit_type
        self.turns = 0
        if self.type == 'G':
            self.enemy_type = 'E'
        else:
            self.enemy_type = 'G'

    def adjacent(self, pos=None):
        if not pos:
            pos = self.pos
        return set((pos[0] + dx, pos[1] + dy) for dy, dx
                   in [(0, -1), (-1, 0), (1, 0), (0, 1)])

    def can_attack(self, units):
        return sorted(
            [u for u in units
             if u.pos in self.adjacent()
             and u.type == self.enemy_type
             and u.alive],
            key=lambda x: (x.hp, x.pos[1], x.pos[0])
        )

    def can_move(self, grid):
        return '.' in [grid[pos] for pos in self.adjacent()]

    def get_enemies(self, units):
        return [u for u in units if u.type == self.enemy_type and u.alive]

    def attack(self, unit):
        unit.take_damage()
        self.turns += 1

    def take_damage(self):
        self.hp -= 3
        if self.hp < 1:
            self.alive = False

    def step(self, grid, step):
        grid[self.pos] = '.'
        grid[step] = self.type
        self.pos = step
        self.turns += 1
        return grid

    def do_nothing(self):
        self.turns += 1

    def shortest_paths(self, grid, units, targets):
        # targets = [u.pos for u in self.get_enemies(units) if u.can_move(grid)]
        occupied = [k for k, v in grid.items() if v != '.' and k != self.pos]
        visited = set(occupied)
        result = []
        best = None
        queue = [(0, [self.pos])]
        while queue:
            distance, path = heapq.heappop(queue)
            if best and len(path) > best:
                return result

            node = path[-1]
            if node in targets:
                result.append(path)
                best = len(path)
                continue

            if node in visited:
                continue

            visited.add(node)
            for neighbor in self.adjacent(node):
                if neighbor in visited:
                    continue
                heapq.heappush(queue, (distance + 1, path + [neighbor]))
        return result


def select_target_step(paths, unit):
    try:
        target_order = sorted(paths, key=lambda x: (x[-1][1], x[-1][0]))
        target_step_order = sorted(
            [p for p in paths if p[-1] == target_order[0][-1]],
            key=lambda x: (x[1][-1], x[1][0])
        )
        return target_step_order[0][-1], target_step_order[0][1]
    except Exception as e:
        raise(e)


def viz_grid(grid):
    y_max = max([k[1] for k, v in grid.items()])
    x_max = max([k[0] for k, v in grid.items()])
    lines = []
    for y in range(y_max + 1):
        line = ''
        for x in range(x_max + 1):
            line += grid[(x, y)]

        lines.append(line)

    return lines


def print_grid(lines=None, grid=None, units=None):
    if not lines:
        lines = viz_grid(grid)
    if grid:
        for i, line in enumerate(lines):
            lu = ['{}({})'.format(u.type, u.hp)
                  for u in sorted(units, key=lambda x: x.pos[0])
                  if u.pos[1] == i]
            if lu:
                line += '   '
                line += ', '.join(lu)
            print(line)
        print('\n')


def print_hp(units):
    print(
        ['{}: {}'.format(u.type, u.hp)
         for u in sorted(units, key=lambda x: (x.pos[1], x.pos[0]))]
    )


def get_max_turns(units):
    return max([u.turns for u in units])


def challenge_15_1(inputs):
    grid = {}
    units = []
    for y, line in enumerate(inputs):
        for x, val in enumerate(line):
            if val in ['G', 'E']:
                units.append(Unit((x, y), val))

            grid[(x, y)] = val

    round_counter = 0
    # print_grid(grid=grid, units=units)
    while True:
        units = sorted(
            [u for u in units if u.alive],
            key=lambda x: (x.pos[1], x.pos[0])
        )
        for unit in units:
            if unit.alive:
                if not unit.get_enemies(units):
                    x = sum([u.hp for u in units if u.alive]) * round_counter
                    return x

                targets = unit.can_attack(units)
                if targets:
                    unit.attack(targets[0])
                    if not targets[0].alive:
                        grid[targets[0].pos] = '.'
                else:
                    targets = [u for u in unit.get_enemies(units)
                               if u.can_move(grid)]
                    if targets and unit.can_move(grid):
                        tc = []
                        for t in targets:
                            tc += [x for x in t.adjacent() if grid[x] == '.']

                        paths = unit.shortest_paths(grid, units, tc)
                        if paths:
                            target, step = select_target_step(paths, unit)
                            grid = unit.step(grid, step)
                            targets = unit.can_attack(units)
                            if targets:
                                unit.attack(targets[0])
                                if not targets[0].alive:
                                    grid[targets[0].pos] = '.'
                        else:
                            unit.do_nothing()
                    else:
                        unit.do_nothing()
                # print_grid(grid=grid, units=units)

        round_counter += 1
        print(round_counter)
        # input('...')

    return None


def challenge_15_2(inputs):
    return None
