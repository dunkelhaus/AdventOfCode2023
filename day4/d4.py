def matches(line):
    div = line.split("|")
    win_str = div[0].split(":")[1].strip()
    my_str = div[1].strip()
    winners = win_str.split(" ")
    my = my_str.split(" ")
    winset = {int(i) for i in winners if i}
    myset = {int(i) for i in my if i}
    count = len(set(winset).intersection(myset))

    return count


def part1():
    result = 0

    with open("./input.txt", "r") as inp:
        for line in inp:
            count = matches(line)

            if count > 0:
                points = 2 ** (count - 1)
            else:
                points = 0

            result += points

    print(f"Part 1: {result}")


def part2():
    counts = []

    with open("./input.txt", "r") as inp:
        for line in inp:
            counts.append(matches(line))

    total = len(counts)
    copies = [1] * total

    for i in range(total):
        for j in range(1, counts[i] + 1):
            if i + j < total:
                copies[i + j] += copies[i]

    print(f"Part 2: {sum(copies)}")


if __name__ == '__main__':
    part1()
    part2()
