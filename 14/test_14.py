from day_14 import challenge_14_1
from day_14 import challenge_14_2


def test_challenge_14_1():
    cases = [
        {
            'inputs': 9,
            'result': '5158916779'
        },
        {
            'inputs': 5,
            'result': '0124515891'
        },
        {
            'inputs': 18,
            'result': '9251071085'
        },
        {
            'inputs': 2018,
            'result': '5941429882'
        }
    ]

    for case in cases:
        assert challenge_14_1(case['inputs']) == case['result']


def test_challenge_14_2():
    cases = [
        {
            'inputs': '51589',
            'result': 9
        },
        {
            'inputs': '01245',
            'result': 5
        },
        {
            'inputs': '92510',
            'result': 18
        },
        {
            'inputs': '59414',
            'result': 2018
        }
    ]

    for case in cases:
        assert challenge_14_2(case['inputs']) == case['result']
