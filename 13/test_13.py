from day_13 import challenge_13_1
from day_13 import challenge_13_2


def test_challenge_13_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_13_1(case['inputs']) == case['result']


def test_challenge_13_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_13_2(case['inputs']) == case['result']
