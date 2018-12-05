from funcs import challenge_03_1
from funcs import challenge_03_2
from funcs import get_inputs_str
from funcs import load_claim


def test_load_claim():
    cases = [
        {
            'text': '#123 @ 3,2: 5x4',
            'result': {
                'claim': 123,
                'x': 3,
                'y': 2,
                'w': 5,
                'h': 4
            }
        }
    ]

    for case in cases:
        assert load_claim(case['text']) == case['result']


def test_challenge_03_1():
    cases = [
        {
            'inputs': [
                '#1 @ 1,3: 4x4',
                '#2 @ 3,1: 4x4',
                '#3 @ 5,5: 2x2'
            ],
            'result': 4
        }
    ]

    for case in cases:
        assert challenge_03_1(case['inputs']) == case['result']


def test_challenge_03_2():
    cases = [
        {
            'inputs': [
                '#1 @ 1,3: 4x4',
                '#2 @ 3,1: 4x4',
                '#3 @ 5,5: 2x2'
            ],
            'result': 3
        }
    ]

    for case in cases:
        assert challenge_03_2(case['inputs']) == case['result']
