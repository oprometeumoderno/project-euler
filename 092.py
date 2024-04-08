from itertools import permutations

CHAIN_CACHE = {1: False, 89: True}


def is_89(n):
    if n in CHAIN_CACHE:
        return CHAIN_CACHE[n]
    else:
        new_n = sum([(int(d) ** 2) for d in str(n)])
        CHAIN_CACHE[n] = is_89(new_n)
        return CHAIN_CACHE[n]


def solution092():
    result = 0
    for i in range(1, 10000000):
        if is_89(i):
            result += 1

    return result
