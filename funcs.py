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


def challenge_02_1(inputs):
    return None


def challenge_02_2(inputs):
    return None
