from common import get_inputs
from day_01 import challenge_01_1
from day_01 import challenge_01_2
from day_01 import challenge_01_2_redux


def test_get_inputs():
    inputs = get_inputs('day_01.txt')
    for x in inputs:
        assert isinstance(x, int)


def test_challenge_01_1():
    cases = [
        {
            'inputs': [1, 1, 1],
            'result': 3
        },
        {
            'inputs': [1, 1, -2],
            'result': 0
        },
        {
            'inputs': [-1, -2, -3],
            'result': -6
        }
    ]

    for case in cases:
        assert challenge_01_1(case['inputs']) == case['result']


def test_challenge_01_2():
    cases = [
        {
            'inputs': [1, -1],
            'result': 0
        },
        {
            'inputs': [3, 3, 4, -2, -4],
            'result': 10
        },
        {
            'inputs': [-6, 3, 8, 5, -6],
            'result': 5
        },
        {
            'inputs': [7, 7, -2, -7, 4],
            'result': 14
        }
    ]

    for case in cases:
        assert challenge_01_2(case['inputs']) == case['result']


def test_challenge_01_2_redux():
    cases = [
        {
            'inputs': [1, -1],
            'result': 0
        },
        {
            'inputs': [3, 3, 4, -2, -4],
            'result': 10
        },
        {
            'inputs': [-6, 3, 8, 5, -6],
            'result': 5
        },
        {
            'inputs': [7, 7, -2, -7, 4],
            'result': 14
        }
    ]

    for case in cases:
        assert challenge_01_2_redux(case['inputs']) == case['result']
