from itertools import permutations

CHAIN_CACHE = {1: False, 89: True}


def is_89_cache(n):
    if n in CHAIN_CACHE:
        return CHAIN_CACHE[n]
    else:
        new_n = sum([(int(d) ** 2) for d in str(n)])
        CHAIN_CACHE[n] = is_89_cache(new_n)
        return CHAIN_CACHE[n]


def solution092():
    result = 0
    for i in range(1, 568):
        if is_89_cache(i):
            result += 1
    for i in range(568, 10000000):
        if CHAIN_CACHE[sum([int(c) ** 2 for c in str(i)])]:
            result += 1
    return result
