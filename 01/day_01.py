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
    sums = set([0])
    current_sum = 0

    while True:
        try:
            current_sum += copy.pop(0)
        except Exception:
            copy = [x for x in inputs]
            current_sum += copy.pop(0)

        if current_sum in sums:
            return current_sum
        else:
            sums.add(current_sum)
