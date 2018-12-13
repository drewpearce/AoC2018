def challenge_02_1(inputs):
    sets = {'2': 0, '3': 0}
    for label in inputs:
        temp = {}
        for char in label:
            if temp.get(char):
                temp[char] += 1
            else:
                temp[char] = 1
        vals = set([v for k, v in temp.items()])
        if 2 in vals:
            sets['2'] += 1
        if 3 in vals:
            sets['3'] += 1
    return sets['2'] * sets['3']


def challenge_02_2(inputs):
    labels = {}
    for x in set(inputs):
        labels.update(
            {
                x: {sum(1 for z in range(0, len(x)) if x[z] != y[z]): y
                    for y in set(inputs)
                    if sum(1 for z in range(0, len(x)) if x[z] != y[z]) == 1}
            }
        )

    labels = {x for x, val in labels.items() if 1 in val.keys()}
    if len(labels) == 2:
        return''.join([x for x in list(labels)[0] if x in list(labels)[1]])
    else:
        return None
