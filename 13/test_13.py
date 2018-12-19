from day_13 import challenge_13_1
from day_13 import challenge_13_2


def test_challenge_13_1():
    cases = [
        {
            'inputs': [
                '/->-\        ',
                '|   |  /----\\',
                '| /-+--+-\  |',
                '| | |  X v  |',
                '\-+-/  \-+--/',
                '  \------/   '
            ],
            'result': (7, 3)
        }
    ]

    for case in cases:
        assert challenge_13_1(case['inputs']) == case['result']


def test_challenge_13_2():
    cases = [
        {
            'inputs': [
                '/>-<\  ',
                '|   |  ',
                '| /<+-\\',
                '| | | v',
                '\>+</ |',
                '  |   ^',
                '  \<->/'
            ],
            'result': (6, 5)
        }
    ]

    for case in cases:
        assert challenge_13_2(case['inputs']) == case['result']
