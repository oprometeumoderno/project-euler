import math


def sorted_index(n: str):
    return "".join(sorted([c for c in n]))


def make_square_anagram(length):
    length_index = {}
    i = math.isqrt(10 ** (length - 1)) + 1
    while len(str(i**2)) <= length:
        index = sorted_index(str(i**2))
        if index in length_index:
            length_index[index].append(i**2)
        else:
            length_index[index] = [i**2]
        i += 1
    if length in [5, 6]:
        return {
            x: length_index[x]
            for x in length_index
            if len(length_index[x]) >= 2 and len(set(x)) >= length - 1
        }
    else:
        return {
            x: length_index[x]
            for x in length_index
            if len(length_index[x]) >= 2 and len(set(x)) == length
        }


def apply_anagram(word, square):
    square = str(square)
    result = {}
    for i in range(len(word)):
        if word[i] not in result:
            result[word[i]] = square[i]
        elif result[word[i]] != square[i]:
            return None
    inverse_result = {}
    for k in result:
        if result[k] not in inverse_result:
            inverse_result[result[k]] = k
        elif inverse_result[result[k]] != k:
            return None
    return result


def solution098():
    with open("input/098.txt") as file:
        anagram_index = {}
        square_index = {}
        words = file.read().split(",")
        words = [w[1:-1] for w in words]
        words[-1] = words[-1][:-1]  # remove trailing newline
        for w in words:
            index = "".join(sorted([c for c in w]))
            if index in anagram_index:
                anagram_index[index].append(w)
            else:
                anagram_index[index] = [w]
    anagram_index = {
        i: anagram_index[i] for i in anagram_index if len(anagram_index[i]) >= 2
    }
    largest_square = 0
    for anagram in anagram_index:
        w_i = len(anagram)
        if w_i not in square_index:
            square_index[w_i] = make_square_anagram(w_i)
        word_1 = anagram_index[anagram][0]
        word_2 = anagram_index[anagram][1]
        for sq_i in square_index[w_i]:
            for i in range(1, len(square_index[w_i][sq_i])):
                for j in range(0, i):
                    sq_1 = square_index[w_i][sq_i][j]
                    sq_2 = square_index[w_i][sq_i][i]
                    mapping_1 = apply_anagram(word_1, sq_1)
                    mapping_2 = apply_anagram(word_2, sq_2)
                    if (
                        mapping_1 is not None
                        and mapping_2 is not None
                        and mapping_1 == mapping_2
                        and max([sq_1, sq_2]) > largest_square
                    ):
                        largest_square = max([sq_1, sq_2])
    return largest_square
