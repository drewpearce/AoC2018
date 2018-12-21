from day_16 import challenge_16_1
from day_16 import challenge_16_2
from day_16 import Instruction
from day_16 import Register


def test_addr():
    reg = Register(r=[12, 0, 4, 13])
    ins = Instruction('addr', 0, 1, 2)
    reg.op(ins)
    assert reg.r == [12, 0, 12, 13]


def test_addi():
    reg = Register(r=[12, 0, 4, 13])
    ins = Instruction('addi', 0, 1, 2)
    reg.op(ins)
    assert reg.r == [12, 0, 13, 13]


def test_mulr():
    reg = Register(r=[3, 5, 22, 4])
    ins = Instruction('mulr', 0, 3, 1)
    reg.op(ins)
    assert reg.r == [3, 12, 22, 4]


def test_muli():
    reg = Register(r=[3, 5, 22, 4])
    ins = Instruction('muli', 0, 3, 1)
    reg.op(ins)
    assert reg.r == [3, 9, 22, 4]


def test_banr():
    reg = Register(r=[5, 34, 7, 31])
    ins = Instruction('banr', 3, 2, 1)
    reg.op(ins)
    assert reg.r == [5, 7, 7, 31]


def test_bani():
    reg = Register(r=[5, 34, 7, 31])
    ins = Instruction('bani', 3, 2, 1)
    reg.op(ins)
    assert reg.r == [5, 2, 7, 31]


def test_borr():
    reg = Register(r=[44, 21, 9, 54])
    ins = Instruction('borr', 0, 3, 2)
    reg.op(ins)
    assert reg.r == [44, 21, 62, 54]


def test_bori():
    reg = Register(r=[44, 21, 9, 54])
    ins = Instruction('bori', 0, 3, 2)
    reg.op(ins)
    assert reg.r == [44, 21, 47, 54]


def test_setr():
    reg = Register(r=[5, 34, 7, 31])
    ins = Instruction('setr', 3, 2, 1)
    reg.op(ins)
    assert reg.r == [5, 31, 7, 31]


def test_seti():
    reg = Register(r=[44, 21, 9, 54])
    ins = Instruction('seti', 0, 3, 2)
    reg.op(ins)
    assert reg.r == [44, 21, 0, 54]


def test_gtir():
    reg = Register(r=[1, 2, 3, 4])
    ins = Instruction('gtir', 1, 2, 3)
    reg.op(ins)
    assert reg.r == [1, 2, 3, 0]


def test_gtri():
    reg = Register(r=[1, 2, 3, 4])
    ins = Instruction('gtri', 1, 1, 3)
    reg.op(ins)
    assert reg.r == [1, 2, 3, 1]


def test_gtrr():
    reg = Register(r=[1, 2, 3, 4])
    ins = Instruction('gtrr', 1, 2, 3)
    reg.op(ins)
    assert reg.r == [1, 2, 3, 0]


def test_eqir():
    reg = Register(r=[1, 2, 1, 2])
    ins = Instruction('eqir', 1, 1, 1)
    reg.op(ins)
    assert reg.r == [1, 0, 1, 2]


def test_eqri():
    reg = Register(r=[1, 2, 1, 2])
    ins = Instruction('eqri', 1, 1, 1)
    reg.op(ins)
    assert reg.r == [1, 0, 1, 2]


def test_eqrr():
    reg = Register(r=[1, 2, 1, 2])
    ins = Instruction('eqrr', 1, 1, 1)
    reg.op(ins)
    assert reg.r == [1, 1, 1, 2]


def test_challenge_16_1():
    cases = [
        {
            'inputs': [
                'Before: [3, 2, 1, 1]',
                '9 2 1 2',
                'After:  [3, 2, 2, 1]'
            ],
            'result': 1
        }
    ]

    for case in cases:
        assert challenge_16_1(case['inputs']) == case['result']


def test_challenge_16_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_16_2(case['inputs']) == case['result']
