import time


def now_ms():
    return int(round(time.time() * 1000))


def log_runtime(start_ms):
    print('Execution took {} ms.'.format(now_ms() - start_ms))


def get_inputs(filename):
    inputs = []
    with open(filename, 'r') as f:
        for line in f:
            inputs.append(int(line))

    return inputs


def challenge_01_1(inputs):
    return sum(inputs)


def challenge_01_2(inputs):
    dupe = False
    sums = [0]
    inc = 0
    while dupe is False:
        freq = sums[-1] + inputs[inc]
        inc += 1
        if freq in sums:
            dupe = freq
            return freq
        else:
            sums.append(freq)

        if inc >= len(inputs):
            inc = 0


def challenge_01_2_redux(inputs):
    copy = [x for x in inputs]
    sums = [0]
    current_sum = 0

    while True:
        try:
            current_sum += copy.pop(0)
        except:
            copy = [x for x in inputs]
            current_sum += copy.pop(0)

        if current_sum in sums:
            return current_sum
        else:
            sums.append(current_sum)


def challenge_02_1(inputs):
    return None


def challenge_02_2(inputs):
    return None
