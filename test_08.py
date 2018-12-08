from funcs import challenge_08_1
from funcs import challenge_08_2


def test_challenge_08_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_08_1(case['inputs']) == case['result']


def test_challenge_08_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_08_2(case['inputs']) == case['result']
