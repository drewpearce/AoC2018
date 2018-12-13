from day_06 import challenge_06_1
from day_06 import challenge_06_2
from day_06 import get_manhattan_distance


def test_get_manhattan_distance():
    assert 5 == get_manhattan_distance((1, 1), (3, 4))


def test_challenge_06_1():
    cases = [
        {
            'inputs': [
                (1, 1),
                (1, 6),
                (8, 3),
                (3, 4),
                (5, 5),
                (8, 9)
            ],
            'result': 17
        }
    ]

    for case in cases:
        assert challenge_06_1(case['inputs']) == case['result']


def test_challenge_06_2():
    cases = [
        {
            'inputs': [
                (1, 1),
                (1, 6),
                (8, 3),
                (3, 4),
                (5, 5),
                (8, 9)
            ],
            'max_distance': 32,
            'result': 16
        }
    ]

    for case in cases:
        test = challenge_06_2(case['inputs'], case['max_distance'])
        assert test == case['result']
