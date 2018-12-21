from day_15 import challenge_15_1
from day_15 import challenge_15_2


def test_challenge_15_1():
    cases = [
        {
            'inputs': ['#######',
                       '#.G...#',
                       '#...EG#',
                       '#.#.#G#',
                       '#..G#E#',
                       '#.....#',
                       '#######'],
            'result': 27730
        },
        {
            'inputs': [
                '#######',
                '#G..#E#',
                '#E#E.E#',
                '#G.##.#',
                '#...#E#',
                '#...E.#',
                '#######'
            ],
            'result': 36334
        },
        {
            'inputs':[
                '#######',
                '#E..EG#',
                '#.#G.E#',
                '#E.##E#',
                '#G..#.#',
                '#..E#.#',
                '#######'
            ],
            'result': 39514
        },
        {
            'inputs': [
                '#######',
                '#E.G#.#',
                '#.#G..#',
                '#G.#.G#',
                '#G..#.#',
                '#...E.#',
                '#######'
            ],
            'result': 27755
        },
        {
            'inputs': [
                '#######',
                '#.E...#',
                '#.#..G#',
                '#.###.#',
                '#E#G#G#',
                '#...#G#',
                '#######'
            ],
            'result': 28944
        },
        {
            'inputs': [
                '#########',
                '#G......#',
                '#.E.#...#',
                '#..##..G#',
                '#...##..#',
                '#...#...#',
                '#.G...G.#',
                '#.....G.#',
                '#########'
            ],
            'result': 18740
        }
    ]

    for case in cases:
        assert challenge_15_1(case['inputs']) == case['result']


def test_challenge_15_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_15_2(case['inputs']) == case['result']
