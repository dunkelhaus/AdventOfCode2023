import math


def get_id_and_turns(game):
    div = game.split(": ")
    game_id = int(div[0].split()[1])
    turns = div[1].split("; ")

    return game_id, turns


def is_valid_game(turns, limits):
    for turn in turns:
        draws = turn.split(", ")

        for draw in draws:
            count, color = draw.split()

            if int(count) > limits[color]:
                return False

    return True


def get_min_counts(game):
    _, turns = get_id_and_turns(game)
    min_counts = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for turn in turns:
        draws = turn.split(", ")

        for draw in draws:
            count, color = draw.split()
            min_counts[color] = max(int(count), min_counts[color])

    return min_counts


def part1():
    id_sum = 0
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    with open("./input.txt", "r") as input:
        for line in input:
            game_id, turns = get_id_and_turns(line)

            if is_valid_game(turns, limits):
                id_sum += game_id

    print(f"Part 1: {id_sum}")


def part2():
    result = 0

    with open("./input.txt", "r") as input:
        for line in input:
            min_counts = get_min_counts(line)
            result += math.prod(min_counts.values())

    print(f"Part 2: {result}")


if __name__ == '__main__':
    part1()
    part2()
