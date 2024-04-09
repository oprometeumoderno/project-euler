import math


def get_prime_factors(n, factors):
    i = 0
    while i < math.isqrt(n):
        if n % (i + 2) == 0:
            return factors[i].union(factors[n // (i + 2) - 2])
        i += 1
    return {n}


def solution047():
    factors = [{2}, {3}]
    distinct_numbers = []
    target = 4
    i = 4

    while len(distinct_numbers) < target:
        distinct_factors = get_prime_factors(i, factors)
        factors.append(distinct_factors)
        if len(distinct_factors) == target:
            distinct_numbers.append(i)
        else:
            distinct_numbers = []
        i += 1
    return distinct_numbers[0]
