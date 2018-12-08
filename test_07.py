from funcs import challenge_07_1
from funcs import challenge_07_2
from funcs import parse_challenge_07_inputs


def test_parse_challenge_07_inputs():
    inputs = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.'
    ]
    correct = [
        {
            'f': 'C',
            'l': 'A'
        },
        {
            'f': 'C',
            'l': 'F'
        },
        {
            'f': 'A',
            'l': 'B'
        },
        {
            'f': 'A',
            'l': 'D'
        },
        {
            'f': 'B',
            'l': 'E'
        },
        {
            'f': 'D',
            'l': 'E'
        },
        {
            'f': 'F',
            'l': 'E'
        }
    ]

    assert parse_challenge_07_inputs(inputs) == correct


def test_challenge_07_1():
    cases = [
        {
            'inputs': [
                'Step C must be finished before step A can begin.',
                'Step C must be finished before step F can begin.',
                'Step A must be finished before step B can begin.',
                'Step A must be finished before step D can begin.',
                'Step B must be finished before step E can begin.',
                'Step D must be finished before step E can begin.',
                'Step F must be finished before step E can begin.'
            ],
            'result': 'CABDFE'
        }
    ]

    for case in cases:
        assert challenge_07_1(case['inputs']) == case['result']


def test_challenge_07_2():
    cases = [
        {
            'inputs': [
                'Step C must be finished before step A can begin.',
                'Step C must be finished before step F can begin.',
                'Step A must be finished before step B can begin.',
                'Step A must be finished before step D can begin.',
                'Step B must be finished before step E can begin.',
                'Step D must be finished before step E can begin.',
                'Step F must be finished before step E can begin.'
            ],
            'w': 2,
            'mod': 0,
            'result': 15
        }
    ]

    for case in cases:
        assert challenge_07_2(case['inputs'], case['w'], case['mod']) == case['result']
