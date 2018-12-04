from funcs import challenge_05_1
from funcs import challenge_05_2


def test_challenge_05_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_05_1(case['inputs']) == case['result']


def test_challenge_05_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_05_2(case['inputs']) == case['result']
