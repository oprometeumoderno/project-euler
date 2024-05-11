def count_values(hand, values):
    value_counts = {}
    for v in [x[0] for x in hand]:
        if v in value_counts:
            value_counts[v] += 1
        else:
            value_counts[v] = 1
    return sorted(
        [(values[v], value_counts[v]) for v in value_counts],
        key=lambda x: 10 ** x[1] + x[0],
        reverse=True,
    )


def count_kinds(hand):
    kind_counts = {}
    for kind in [x[1] for x in hand]:
        if kind in kind_counts:
            kind_counts[kind] += 1
        else:
            kind_counts[kind] = 1
    return [(kind, kind_counts) for kind in kind_counts]


def is_royal_straight_flush(hand, values):
    if (
        sorted([x[0] for x in hand], key=lambda x: values[x])
        == [
            "T",
            "J",
            "Q",
            "K",
            "A",
        ]
        and len(count_kinds(hand)) == 1
    ):
        return True


def is_straight(hand, values):
    sorted_cards = sorted([x[0] for x in hand], key=lambda x: values[x])
    for i in range(1, len(sorted_cards)):
        if values[sorted_cards[i]] - values[sorted_cards[i - 1]] != 1:
            return False
    return True


def is_straight_flush(hand, values):
    sorted_cards = sorted([x[0] for x in hand], key=lambda x: values[x])
    if len(count_kinds(hand)) > 1:
        return False
    for i in range(1, len(sorted_cards)):
        if values[sorted_cards[i]] - values[sorted_cards[i - 1]] != 1:
            return False

    return True


def get_score(hand, values):
    value_counts = count_values(hand, values)

    # royal straight flush
    if is_royal_straight_flush(hand, values):
        return None, 10

    # straight flush
    if is_straight_flush(hand, values):
        return value_counts, 9

    # four of a kind
    if len(value_counts) == 2 and value_counts[0][1] == 4:
        return value_counts, 8

    # full house
    if len(value_counts) == 2 and value_counts[0][1] == 3:
        return sorted(value_counts, key=lambda x: x[0], reverse=True), 7

    # flush
    if len(count_kinds(hand)) == 1:
        return value_counts, 6

    # straight
    if is_straight(hand, values):
        return value_counts, 5

    # three of a kind
    if len(value_counts) == 3 and value_counts[0][1] == 3:
        return value_counts, 4

    # two pairs
    if len(value_counts) == 3 and value_counts[0][1] == 2:
        return value_counts, 3

    # pair
    if len(value_counts) == 4 and value_counts[0][1] == 2:
        return value_counts, 2

    else:
        return value_counts, 0


def solution054():
    values = {str(x): x for x in range(2, 10)}
    values.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})
    result = 0
    with open("input/054.txt", "r") as file:
        lines = file.read().split("\n")[:-1]
        for hands in lines:
            cards = hands.split(" ")
            hand_left = cards[0:5]
            hand_right = cards[5:]
            cards_l, score_l = get_score(hand_left, values)
            cards_r, score_r = get_score(hand_right, values)

            if score_l > score_r:
                result += 1
            elif score_r == score_l:
                i = 0
                while cards_l[i][0] == cards_r[i][0]:
                    i += 1
                if cards_l[i][0] > cards_r[i][0]:
                    result += 1

    return result
