from funcs import challenge_04_1
from funcs import challenge_04_2


def test_challenge_04_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_04_1(case['inputs']) == case['result']


def test_challenge_04_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_04_2(case['inputs']) == case['result']
