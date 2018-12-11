from day_08 import challenge_08_1
from day_08 import challenge_08_2


def test_challenge_08_1():
    cases = [
        {
            'inputs': '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2',
            'result': 138
        }
    ]

    for case in cases:
        assert challenge_08_1(case['inputs']) == case['result']


def test_challenge_08_2():
    cases = [
        {
            'inputs': '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2',
            'result': 66
        }
    ]

    for case in cases:
        assert challenge_08_2(case['inputs']) == case['result']
