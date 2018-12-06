from funcs import challenge_06_1
from funcs import challenge_06_2


def test_challenge_06_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_06_1(case['inputs']) == case['result']


def test_challenge_06_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_06_2(case['inputs']) == case['result']
