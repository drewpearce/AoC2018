from collections import defaultdict
from collections import deque


def play_marble_game(players, marble_max):
    board = deque([0])
    scores = defaultdict(int)
    for marble in range(1, marble_max + 1):
        current_player = marble % players

        if marble % 23 == 0:
            board.rotate(7)
            scores[current_player] += marble + board.pop()
            board.rotate(-1)
        else:
            board.rotate(-1)
            board.append(marble)

    return sorted([v for k, v in scores.items()], reverse=True)[0]


def challenge_09_1(inputs):
    players = int(inputs.split(' ')[0])
    marble_max = int(inputs.split(' ')[-2])
    return play_marble_game(players, marble_max)


def challenge_09_2(inputs):
    players = int(inputs.split(' ')[0])
    marble_max = int(inputs.split(' ')[-2]) * 100
    return play_marble_game(players, marble_max)
