from funcs import challenge_10_parse_inputs


def get_test_inputs():
    return [
                'position=< 9,  1> velocity=< 0,  2>',
                'position=< 7,  0> velocity=<-1,  0>',
                'position=< 3, -2> velocity=<-1,  1>',
                'position=< 6, 10> velocity=<-2, -1>',
                'position=< 2, -4> velocity=< 2,  2>',
                'position=<-6, 10> velocity=< 2, -2>',
                'position=< 1,  8> velocity=< 1, -1>',
                'position=< 1,  7> velocity=< 1,  0>',
                'position=<-3, 11> velocity=< 1, -2>',
                'position=< 7,  6> velocity=<-1, -1>',
                'position=<-2,  3> velocity=< 1,  0>',
                'position=<-4,  3> velocity=< 2,  0>',
                'position=<10, -3> velocity=<-1,  1>',
                'position=< 5, 11> velocity=< 1, -2>',
                'position=< 4,  7> velocity=< 0, -1>',
                'position=< 8, -2> velocity=< 0,  1>',
                'position=<15,  0> velocity=<-2,  0>',
                'position=< 1,  6> velocity=< 1,  0>',
                'position=< 8,  9> velocity=< 0, -1>',
                'position=< 3,  3> velocity=<-1,  1>',
                'position=< 0,  5> velocity=< 0, -1>',
                'position=<-2,  2> velocity=< 2,  0>',
                'position=< 5, -2> velocity=< 1,  2>',
                'position=< 1,  4> velocity=< 2,  1>',
                'position=<-2,  7> velocity=< 2, -2>',
                'position=< 3,  6> velocity=<-1, -1>',
                'position=< 5,  0> velocity=< 1,  0>',
                'position=<-6,  0> velocity=< 2,  0>',
                'position=< 5,  9> velocity=< 1, -2>',
                'position=<14,  7> velocity=<-2,  0>',
                'position=<-3,  6> velocity=< 2, -1>',
            ]


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
