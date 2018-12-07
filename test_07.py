from funcs import challenge_07_1
from funcs import challenge_07_2


def test_challenge_07_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_07_1(case['inputs']) == case['result']


def test_challenge_07_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_07_2(case['inputs']) == case['result']
