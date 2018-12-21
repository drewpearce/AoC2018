scores = '37'
e1 = 0
e2 = 1


def iterate_recipes():
    global scores
    global e1
    global e2
    new = str(int(scores[e1]) + int(scores[e2]))
    scores += new
    e1 = (e1 + 1 + int(scores[e1])) % len(scores)
    e2 = (e2 + 1 + int(scores[e2])) % len(scores)


def challenge_14_1(inputs):
    while len(scores) < int(inputs) + 10:
        iterate_recipes()

    return scores[int(inputs):int(inputs) + 10]


def challenge_14_2(inputs):
    while inputs not in scores[-len(inputs):]:
        iterate_recipes()
        if len(scores) % 1000000 == 0:
            print(len(scores))
        if len(scores) > 21000000:
            break

    return scores.index(inputs)
