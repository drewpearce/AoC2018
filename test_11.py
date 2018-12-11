from day_11 import challenge_11_1
from day_11 import challenge_11_2


def test_challenge_11_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_11_1(case['inputs']) == case['result']


def test_challenge_11_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_11_2(case['inputs']) == case['result']
