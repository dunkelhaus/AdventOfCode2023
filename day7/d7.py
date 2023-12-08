from itertools import chain
from collections import Counter


def get_ordered_counts(counts, order, joker):
    ordered_counts = None

    if joker and 'J' in counts and counts['J'] < 5:
        joker_count = counts.pop('J')
        ordered_counts = counts.most_common()
        ordered_counts[0] = (
            ordered_counts[0][0],
            ordered_counts[0][1] + joker_count
        )
    else:
        ordered_counts = counts.most_common()

    return ordered_counts


def populate_hand_map(hand, hand_map, ordered_counts):
    buckets = len(ordered_counts)

    if buckets == 1:
        hand_map["five"].append(hand)
    elif buckets == 2 and ordered_counts[0][1] == 4:
        hand_map["four"].append(hand)
    elif buckets == 2 and ordered_counts[0][1] == 3:
        hand_map["full"].append(hand)
    elif buckets == 3 and ordered_counts[0][1] == 3:
        hand_map["three"].append(hand)
    elif buckets == 3 and ordered_counts[0][1] == 2:
        hand_map["two"].append(hand)
    elif buckets == 4:
        hand_map["one"].append(hand)
    elif buckets == 5:
        hand_map["top"].append(hand)
    else:
        print(f"Unknown hand found: {hand}")

    return hand_map


def get_hand_map(file, order, joker):
    hand_strengths = ['top', 'one', 'two', 'three', 'full', 'four', 'five']
    hand_map = {i: [] for i in hand_strengths}

    with open(file, "r") as input:
        for line in input:
            hand = tuple(line.split())
            counts = Counter(hand[0])
            ordered_counts = get_ordered_counts(counts, order, joker)
            hand_map = populate_hand_map(hand, hand_map, ordered_counts)

    return hand_map


def sort_hand_map(hand_map, order):
    alphabet = {order[i]: i for i in range(len(order))}

    for hand_type, hands in hand_map.items():
        hand_map[hand_type] = sorted(
            hands,
            key=lambda word: [alphabet[letter] for letter in word[0]]
        )

    return hand_map


def winnings(hands_file, joker=False):
    result = 0
    order = "J23456789TQKA" if joker else "23456789TJQKA"

    hand_map = get_hand_map(hands_file, order, joker)
    sorted_hand_map = sort_hand_map(hand_map, order)

    flat_list = list(chain.from_iterable(sorted_hand_map.values()))

    for i in range(len(flat_list)):
        result += int(flat_list[i][1]) * (i + 1)

    return result


def part1(hands_file):
    print(f"Part 1: {winnings(hands_file)}")


def part2(hands_file):
    print(f"Part 2: {winnings(hands_file, joker=True)}")


if __name__ == '__main__':
    part1('input.txt')
    part2('input.txt')
