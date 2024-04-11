from functools import reduce
import operator


def solution053():
    FACTORIAL_CACHE = []
    for i in range(1, 101):
        FACTORIAL_CACHE.append(reduce(operator.mul, list(range(1, i + 1))))

    result = 0
    for n in range(101):
        for r in range(n + 1):
            if (
                FACTORIAL_CACHE[n - 1]
                / (FACTORIAL_CACHE[r - 1] * FACTORIAL_CACHE[n - r - 1])
                > 1000000
            ):
                result += 1
    return result
