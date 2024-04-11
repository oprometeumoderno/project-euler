CHAIN_CACHE = [False] * 1000
CHAIN_CACHE[1] = 0
CHAIN_CACHE[89] = 1


def is_89_cache(n):
    if n == 1:
        return 0
    elif n == 89:
        return True
    new_n = sum([(int(d) ** 2) for d in str(n)])
    CHAIN_CACHE[n] = is_89_cache(new_n)
    return CHAIN_CACHE[new_n]


def solution092():
    result = 0
    for n in range(1, 1000):
        result += is_89_cache(n)

    for n in range(1000, 10000000, 10):
        index = 0
        while n > 0:
            index += (n % 10) ** 2
            n //= 10
        result += (
            CHAIN_CACHE[index]
            + CHAIN_CACHE[index + 1]
            + CHAIN_CACHE[index + 4]
            + CHAIN_CACHE[index + 9]
            + CHAIN_CACHE[index + 16]
            + CHAIN_CACHE[index + 25]
            + CHAIN_CACHE[index + 36]
            + CHAIN_CACHE[index + 49]
            + CHAIN_CACHE[index + 64]
            + CHAIN_CACHE[index + 81]
        )

    return result
