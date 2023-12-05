import itertools


def get_surrounding_coords(i, j):
    rows = range(i - 1, i + 2)
    cols = range(j - 1, j + 2)

    return itertools.product(rows, cols)


def look_around(i, j, data):
    for row, col in get_surrounding_coords(i, j):
        if data[row][col].isdigit():
            print(f"digit! at: {row} {col}")


def part1(data):
    # symbols = set.union(*[set(i) for i in data])

    for i in range(len(data)):
        for j in range(len(data[i])):
            if not data[i][j].isalnum() and data[i][j] != '.':
                look_around(i, j, data)


if __name__ == '__main__':
    data = []

    with open("./input.txt", "r") as input:
        for line in input:
            data.append(list(line.rstrip()))

    part1(data)
