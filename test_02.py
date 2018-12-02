from funcs import challenge_02_1
from funcs import challenge_02_2a
from funcs import get_inputs


def test_get_inputs():
    inputs = get_inputs('day_02.txt')
    for x in inputs:
        assert isinstance(x, int)


def test_challenge_02_1():
    cases = [
        {
            'inputs': ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd',
                       'abcdee', 'ababab'],
            'result': 12
        }
    ]

    for case in cases:
        assert challenge_02_1(case['inputs']) == case['result']


def test_challenge_02_2():
    cases = [
        {
            'inputs': ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye',
                       'wvxyz'],
            'result': 'fgij'
        }
    ]

    for case in cases:
        assert challenge_02_2(case['inputs']) == case['result']
