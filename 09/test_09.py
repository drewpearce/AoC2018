from day_09 import challenge_09_1


def test_challenge_09_1():
    cases = [
        {
            'inputs': '9 players; last marble is worth 25 points',
            'result': 32
        },
        {
            'inputs': '10 players; last marble is worth 1618 points',
            'result': 8317
        },
        {
            'inputs': '13 players; last marble is worth 7999 points',
            'result': 146373
        },
        {
            'inputs': '17 players; last marble is worth 1104 points',
            'result': 2764
        },
        {
            'inputs': '21 players; last marble is worth 6111 points',
            'result': 54718
        },
        {
            'inputs': '30 players; last marble is worth 5807 points',
            'result': 37305
        }
    ]

    for case in cases:
        assert challenge_09_1(case['inputs']) == case['result']
