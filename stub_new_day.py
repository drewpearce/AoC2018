# Tool to stub out the repo with functions and files for a day's challenge.
# Example usage: python stub_new_day.py 09
# Would create day_09.txt, day_09.py, test_09.py, and append to funcs.py


import os
import sys

DAY_NUM = sys.argv[1]  # provide day number as cmd line argument
DAY = 'day_' + DAY_NUM
PATH = os.path.abspath(os.path.dirname(__file__)) + '/'
NEW_FUNCS = '''

def challenge_{DAY}_1(inputs):
    return None


def challenge_{DAY}_2(inputs):
    return None
'''
NEW_TESTS = '''from funcs import challenge_{DAY}_1
from funcs import challenge_{DAY}_2


def test_challenge_{DAY}_1():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_{DAY}_1(case['inputs']) == case['result']


def test_challenge_{DAY}_2():
    cases = [
        {
            'inputs': [],
            'result': True
        }
    ]

    for case in cases:
        assert challenge_{DAY}_2(case['inputs']) == case['result']
'''
NEW_RUN = '''from funcs import challenge_{DAY}_1
from funcs import challenge_{DAY}_2
from funcs import get_inputs
from funcs import get_inputs_str
from funcs import log_runtime
from funcs import now_ms


inputs = get_inputs('day_{DAY}.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_{DAY}_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_{DAY}_2(inputs)))
log_runtime(start_ms)
'''


def write_text_file():
    with open(PATH + DAY + '.txt', 'w') as f:
        f.write('')


def append_new_funcs():
    with open(PATH + 'funcs.py', 'a') as f:
        f.write(NEW_FUNCS.replace('{DAY}', DAY_NUM))


def write_test_file():
    with open(PATH + 'test_' + DAY_NUM + '.py', 'w') as f:
        f.write(NEW_TESTS.replace('{DAY}', DAY_NUM))


def write_run_file():
    with open(PATH + DAY + '.py', 'w') as f:
        f.write(NEW_RUN.replace('{DAY}', DAY_NUM))


print('Writing text file...')
write_text_file()
print('Appending new functions...')
append_new_funcs()
print('Writing test file...')
write_test_file()
print('Writing run file...')
write_run_file()
