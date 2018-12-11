from day_10 import challenge_10_parse_inputs
from day_10 import get_test_inputs


def test_challenge_10_parse_inputs():
    cases = [
        {
            'inputs': get_test_inputs(),
            'result': [
                {'v_x': 0, 'v_y': 2, 'x': 9, 'y': 1},
                {'v_x': -1, 'v_y': 0, 'x': 7, 'y': 0},
                {'v_x': -1, 'v_y': 1, 'x': 3, 'y': -2},
                {'v_x': -2, 'v_y': -1, 'x': 6, 'y': 10},
                {'v_x': 2, 'v_y': 2, 'x': 2, 'y': -4},
                {'v_x': 2, 'v_y': -2, 'x': -6, 'y': 10},
                {'v_x': 1, 'v_y': -1, 'x': 1, 'y': 8},
                {'v_x': 1, 'v_y': 0, 'x': 1, 'y': 7},
                {'v_x': 1, 'v_y': -2, 'x': -3, 'y': 11},
                {'v_x': -1, 'v_y': -1, 'x': 7, 'y': 6},
                {'v_x': 1, 'v_y': 0, 'x': -2, 'y': 3},
                {'v_x': 2, 'v_y': 0, 'x': -4, 'y': 3},
                {'v_x': -1, 'v_y': 1, 'x': 10, 'y': -3},
                {'v_x': 1, 'v_y': -2, 'x': 5, 'y': 11},
                {'v_x': 0, 'v_y': -1, 'x': 4, 'y': 7},
                {'v_x': 0, 'v_y': 1, 'x': 8, 'y': -2},
                {'v_x': -2, 'v_y': 0, 'x': 15, 'y': 0},
                {'v_x': 1, 'v_y': 0, 'x': 1, 'y': 6},
                {'v_x': 0, 'v_y': -1, 'x': 8, 'y': 9},
                {'v_x': -1, 'v_y': 1, 'x': 3, 'y': 3},
                {'v_x': 0, 'v_y': -1, 'x': 0, 'y': 5},
                {'v_x': 2, 'v_y': 0, 'x': -2, 'y': 2},
                {'v_x': 1, 'v_y': 2, 'x': 5, 'y': -2},
                {'v_x': 2, 'v_y': 1, 'x': 1, 'y': 4},
                {'v_x': 2, 'v_y': -2, 'x': -2, 'y': 7},
                {'v_x': -1, 'v_y': -1, 'x': 3, 'y': 6},
                {'v_x': 1, 'v_y': 0, 'x': 5, 'y': 0},
                {'v_x': 2, 'v_y': 0, 'x': -6, 'y': 0},
                {'v_x': 1, 'v_y': -2, 'x': 5, 'y': 9},
                {'v_x': -2, 'v_y': 0, 'x': 14, 'y': 7},
                {'v_x': 2, 'v_y': -1, 'x': -3, 'y': 6}
            ]
        }
    ]

    for case in cases:
        assert challenge_10_parse_inputs(case['inputs']) == case['result']
