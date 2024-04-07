from itertools import permutations

d_8910 = [x for x in range(100, 1000) if x % 17 == 0]
d_789 = [x for x in range(100, 1000) if x % 13 == 0]


def has_repeated_digit(n):
    digits = set()
    while n != "":
        if n[0] in digits:
            return True
        else:
            digits.add(n[0])
            n = n[1:]
    return False


def solution043():
    result = 0
    sequences_78910 = set()
    for d_17 in d_8910:
        possible_pairs = [x for x in d_789 if x % 100 == d_17 // 10]

        if possible_pairs:
            sequences_78910.update([f"{x}{d_17 % 10}" for x in possible_pairs])

    possible_sequences = [x for x in sequences_78910 if not has_repeated_digit(x)]
    possible_sequences_11 = []
    for possible_sequence in possible_sequences:
        for i in range(0, 10):
            if (
                str(i) not in possible_sequence
                and int(f"{i}{possible_sequence[0:2]}") % 11 == 0
            ):
                possible_sequences_11.append(f"{i}{possible_sequence}")
    possible_sequences_11 = [x for x in possible_sequences_11 if x[0] in ["0", "5"]]

    possible_sequences_7 = []
    for possible_sequence in possible_sequences_11:
        for i in range(0, 10):
            if (
                str(i) not in possible_sequence
                and int(f"{i}{possible_sequence[0:2]}") % 7 == 0
            ):
                possible_sequences_7.append(f"{i}{possible_sequence}")

    for possible_seq7 in possible_sequences_7:
        possible_digits = set([str(x) for x in range(0, 10)]) - set(
            [x for x in possible_seq7]
        )
        for permutation in permutations(possible_digits):
            number = "".join(permutation) + possible_seq7

            if (
                int(f"{number[1]}{number[2]}{number[3]}") % 2 == 0
                and int(f"{number[2]}{number[3]}{number[4]}") % 3 == 0
            ):
                result += int(number)

    return result
