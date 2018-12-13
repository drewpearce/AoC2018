
TEST_IN = [
    'initial state: #..#.#..##......###...###',
    '',
    '...## => #',
    '..#.. => #',
    '.#... => #',
    '.#.#. => #',
    '.#.## => #',
    '.##.. => #',
    '.#### => #',
    '#.#.# => #',
    '#.### => #',
    '##.#. => #',
    '##.## => #',
    '###.. => #',
    '###.# => #',
    '####. => #'
]


def parse_inputs(inputs):
    state = inputs[0].split(' ')[2]
    rules = {}
    for x in inputs[1:]:
        if x != '':
            rules[x.split(' ')[0]] = x.split(' ')[2]

    return state, rules


def iterate_generations(state, rules, gen):
    pos_move = 0
    for _ in range(gen):
        new = ''
        if state[0] == '#':
            state = '...' + state
            pos_move += 3
        if state[-1] == '#':
            state += '...'
        for i, p in enumerate(state):
            if i < 2:
                temp = state[0:i + 1]
                while len(temp) < 3:
                    temp = '.' + temp
                temp += state[i + 1: i + 3]
            elif i >= len(state) - 2:
                temp = state[i:]
                while len(temp) < 3:
                    temp += '.'
                temp = state[i - 2: i] + temp
            else:
                temp = state[i - 2: i + 3]

            if rules.get(temp):
                new += rules[temp]
            else:
                new += '.'

        state = new

    return (state, pos_move)


def find_recurrence(inputs):
    state, rules = parse_inputs(inputs)
    x = 1
    comp = state.replace('.', ' ').strip()
    while True:
        results = iterate_generations(state, rules, x)
        temp = results[0].replace('.', ' ').strip()
        if temp == comp:
            return x - 1
        else:
            comp = temp
            x += 1


def challenge_12_1(inputs, gen):
    state, rules = parse_inputs(inputs)
    results = iterate_generations(state, rules, gen)
    return sum([i - results[1] for i, x in enumerate(results[0]) if x == '#'])


def challenge_12_2(inputs, gen):
    recurrence = find_recurrence(inputs)
    vals = [challenge_12_1(inputs, x)
            for x in range(recurrence, recurrence + 10)]
    difs = [vals[x] - vals[x - 1] for x in range(1, len(vals))]
    if len(set(difs)) == 1:
        dif = difs[0]
    else:
        raise Exception('Inconsisten difference. Re-evaluate recurrence.')

    return (gen - recurrence) * dif + vals[0]
