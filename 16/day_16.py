class Instruction(object):
    def __init__(self, opcode, a, b, c):
        self.opcode = opcode
        self.a = a
        self.b = b
        self.c = c


class Register(object):
    def __init__(self, r=None):
        if not r:
            self.r = [0, 0, 0, 0]
        else:
            self.r = r

        self.op_map = {
            'addr': self.addr,
            'addi': self.addi,
            'mulr': self.mulr,
            'muli': self.muli,
            'banr': self.banr,
            'bani': self.bani,
            'borr': self.borr,
            'bori': self.bori,
            'setr': self.setr,
            'seti': self.seti,
            'gtir': self.gtir,
            'gtri': self.gtri,
            'gtrr': self.gtrr,
            'eqir': self.eqir,
            'eqri': self.eqri,
            'eqrr': self.eqrr
        }

    def addr(self, a, b, c):
        self.r[c] = self.r[a] + self.r[b]

    def addi(self, a, b, c):
        self.r[c] = self.r[a] + b

    def mulr(self, a, b, c):
        self.r[c] = self.r[a] * self.r[b]

    def muli(self, a, b, c):
        self.r[c] = self.r[a] * b

    def banr(self, a, b, c):
        self.r[c] = self.r[a] & self.r[b]

    def bani(self, a, b, c):
        self.r[c] = self.r[a] & b

    def borr(self, a, b, c):
        self.r[c] = self.r[a] | self.r[b]

    def bori(self, a, b, c):
        self.r[c] = self.r[a] | b

    def setr(self, a, b, c):
        self.r[c] = self.r[a]

    def seti(self, a, b, c):
        self.r[c] = a

    def gtir(self, a, b, c):
        self.r[c] = int(a > self.r[b])

    def gtri(self, a, b, c):
        self.r[c] = int(self.r[a] > b)

    def gtrr(self, a, b, c):
        self.r[c] = int(self.r[a] > self.r[b])

    def eqir(self, a, b, c):
        self.r[c] = int(a == self.r[b])

    def eqri(self, a, b, c):
        self.r[c] = int(self.r[a] == b)

    def eqrr(self, a, b, c):
        self.r[c] = int(self.r[a] == self.r[b])

    def op(self, i):
        return self.op_map[i.opcode](i.a, i.b, i.c)


def process_inputs(inputs):
    tests = []
    test = {}
    id = 0
    empty_count = 0
    for _ in range(len(inputs)):
        line = inputs.pop(0)
        if line.startswith('Before'):
            test['start'] = [int(x) for x in
                             line.split('[')[1][0:-1].split(', ')]
            empty_count = 0
        elif line.startswith('After'):
            test['end'] = [int(x) for x in
                           line.split('[')[1][0:-1].split(', ')]
            empty_count = 0
        elif line == '':
            empty_count += 1
        else:
            test['input'] = [int(x) for x in line.split(' ')]
            empty_count = 0

        if empty_count == 2:
            test = {}
            break

        if test.get('start') and test.get('end') and test.get('input'):
            test['id'] = id
            tests.append(test)
            test = {}
            id += 1

    return tests


def challenge_16_1(inputs):
    tests = process_inputs([x for x in inputs])
    test_results = []
    for test in tests:
        matches = []
        for k, v in Register().op_map.items():
            reg = Register(r=[x for x in test['start']])
            ins = Instruction(k, test['input'][1], test['input'][2],
                              test['input'][3])
            reg.op(ins)
            if reg.r == test['end']:
                matches.append(k)
        test_results.append({
            'id': test['id'],
            'matches': matches
        })

    return sum(1 for x in test_results if len(x['matches']) >= 3)


def challenge_16_2(inputs):
    tests = process_inputs(inputs)
    test_results = []
    for test in tests:
        matches = []
        for k, v in Register().op_map.items():
            reg = Register(r=[x for x in test['start']])
            ins = Instruction(k, test['input'][1], test['input'][2],
                              test['input'][3])
            reg.op(ins)
            if reg.r == test['end']:
                matches.append(k)
        test_results.append({
            'id': test['id'],
            'matches': matches,
            'op_id': test['input'][0]
        })

    op_map = [None for x in range(16)]
    matched = set([])
    matches = {}
    for t in test_results:
        if not matches.get(t['op_id']):
            matches[t['op_id']] = set(t['matches'])
        else:
            for m in t['matches']:
                matches[t['op_id']].add(m)

    while len([x for x in op_map if x is None]) > 0:
        for k, v in matches.items():
            v.difference_update(matched)

        for k, v in matches.items():
            if len(v) == 1:
                op_map[k] = v.pop()
                matched.add(op_map[k])

    r = Register()
    inputs = [Instruction(op_map[int(x[0])], int(x[1]), int(x[2]), int(x[3]))
              for x in (i.split() for i in inputs if i != '')]
    for i in inputs:
        r.op(i)

    return r.r[0]
