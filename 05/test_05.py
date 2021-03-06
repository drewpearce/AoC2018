from day_05 import challenge_05_1
from day_05 import challenge_05_1_redux
from day_05 import challenge_05_2
from day_05 import challenge_05_2_redux
from day_05 import generate_regex


def test_generate_regex():
    assert generate_regex() == ('aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|'
                                'Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|'
                                'pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|'
                                'Ww|xX|Xx|yY|Yy|zZ|Zz')


def test_challenge_05_1():
    cases = [
        {
            'inputs': 'dabAcCaCBAcCcaDA',
            'result': 10
        }
    ]

    for case in cases:
        assert challenge_05_1(case['inputs']) == case['result']


def test_challenge_05_1_redux():
    cases = [
        {
            'inputs': 'dabAcCaCBAcCcaDA',
            'result': 10
        }
    ]

    for case in cases:
        assert challenge_05_1_redux(case['inputs']) == case['result']


def test_challenge_05_2():
    cases = [
        {
            'inputs': 'dabAcCaCBAcCcaDA',
            'result': 4
        }
    ]

    for case in cases:
        assert challenge_05_2(case['inputs']) == case['result']


def test_challenge_05_2_reduz():
    cases = [
        {
            'inputs': 'dabAcCaCBAcCcaDA',
            'result': 4
        }
    ]

    for case in cases:
        assert challenge_05_2_redux(case['inputs']) == case['result']
