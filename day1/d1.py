def part1():
    result = 0
    with open("./input.txt", "r") as inp:
        for line in inp:
            upper = len(line)
            bptr = upper - 1
            fptr = 0
            front = False
            back = False

            while not front or not back:
                if not front:
                    if line[fptr].isdigit():
                        front = True
                    else:
                        fptr += 1
                if not back:
                    if line[bptr].isdigit():
                        back = True
                    else:
                        bptr -= 1

            result += int(line[fptr] + line[bptr])

    print(f"Part 1: {result}")


def make_trie(words):
    trie = {}
    inner_trie = trie

    for word in words:
        for letter in word:
            if letter not in inner_trie:
                inner_trie[letter] = {}
            inner_trie = inner_trie[letter]

        inner_trie["end"] = word
        inner_trie = trie

    return trie


def find(trie, line, start, rev):
    subtrie = trie
    upper = len(line)
    step = 1

    if rev:
        upper = -1
        step = -1

    for i in range(start, upper, step):
        if line[i] in subtrie:
            subtrie = subtrie[line[i]]
        elif "end" in subtrie:
            return subtrie["end"]
        else:
            return ""

    return ""


def part2():
    result = 0
    accepted = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    accepted_rev = [item[::-1] for item in accepted]
    forward = make_trie(accepted)
    backward = make_trie(accepted_rev)
    string_nums = [str(i) for i in range(1, 10)]
    number_map = dict(zip(accepted, string_nums))
    number_map[""] = ""

    with open("./input.txt", "r") as inp:
        for line in inp:
            upper = len(line)
            bptr = upper - 1
            fptr = 0
            front = ""
            back = ""

            while not front or not back:
                if not front:
                    if line[fptr].isdigit():
                        front = line[fptr]
                    elif line[fptr] in forward:
                        front = number_map[find(forward, line, fptr, False)]
                    fptr += 1
                if not back:
                    if line[bptr].isdigit():
                        back = line[bptr]
                    elif line[bptr] in backward:
                        back = number_map[find(backward, line, bptr, True)[::-1]]
                    bptr -= 1

            result += int(front + back)

    print(f"Part 2: {result}")


if __name__ == '__main__':
    part1()
    part2()
