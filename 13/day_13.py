U = (0, -1)
D = (0, 1)
L = (-1, 0)
R = (1, 0)
direction_map = {
    '^': U,
    'v': D,
    '<': L,
    '>': R
}
reverse_map = {v: k for k, v in direction_map.items()}
straight = {
    U: U,
    D: D,
    L: L,
    R: R
}
left_turn = {
    U: L,
    D: R,
    L: D,
    R: U
}
right_turn = {
    U: R,
    D: L,
    L: U,
    R: D
}
slash_turn = {
    U: R,
    D: L,
    L: D,
    R: U
}
backslash_turn = {
    U: L,
    D: R,
    L: U,
    R: D
}


class Cart(object):
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
        self.turns = 0
        self.alive = True

    def step(self, grid):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        coord = grid[self.pos]
        if coord == '+':
            turn_choice = [
                left_turn,
                straight,
                right_turn
            ][self.turns % 3]
            self.dir = turn_choice[self.dir]
            self.turns += 1
        elif coord == '/':
            self.dir = slash_turn[self.dir]
        elif coord == '\\':
            self.dir = backslash_turn[self.dir]

    def collide(self, other_cart):
        if (other_cart != self and self.alive and other_cart.alive
                and self.pos == other_cart.pos):
            return True
        else:
            return False


def print_grid(grid, carts):
    y_max = max([k[1] for k, v in grid.items()])
    x_max = max([k[0] for k, v in grid.items()])
    for y in range(y_max + 1):
        line = ''
        for x in range(x_max + 1):
            c = None
            for cart in carts:
                if cart.pos == (x, y) and cart.alive:
                    c = reverse_map[cart.dir]
            if not c:
                c = grid[(x, y)]
            line += c
        print(line)


def challenge_13_1(inputs):
    grid = {}
    carts = []
    for y, line in enumerate(inputs):
        for x, val in enumerate(line):
            if val in direction_map:
                carts.append(Cart((x, y), direction_map[val]))
                if val in ['^', 'v']:
                    grid[(x, y)] = '|'
                elif val in ['<', '>']:
                    grid[(x, y)] = '-'
            else:
                grid[(x, y)] = val

    while True:
        carts = sorted(carts, key=lambda x: (x.pos[1], x.pos[0]))
        for cart in carts:
            if cart.alive:
                cart.step(grid)
                # print_grid(grid, carts)
                for other_cart in carts:
                    if cart.collide(other_cart):
                        return cart.pos


def challenge_13_2(inputs):
    grid = {}
    carts = []
    for y, line in enumerate(inputs):
        for x, val in enumerate(line):
            if val in direction_map:
                carts.append(Cart((x, y), direction_map[val]))
                if val in ['^', 'v']:
                    grid[(x, y)] = '|'
                elif val in ['<', '>']:
                    grid[(x, y)] = '-'
            else:
                grid[(x, y)] = val

    while True:
        carts = sorted(carts, key=lambda x: (x.pos[1], x.pos[0]))
        for cart in carts:
            if cart.alive:
                cart.step(grid)
                # print_grid(grid, carts)
                for other_cart in carts:
                    if cart.collide(other_cart):
                        cart.alive = False
                        other_cart.alive = False
                        if len([cart for cart in carts if cart.alive]) == 1:
                            return [cart for cart in carts
                                    if cart.alive][0].pos
