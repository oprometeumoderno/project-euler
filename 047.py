def get_prime_factors(n, primes):
    current_prime = 0
    i = n
    factors = {}
    while current_prime < len(primes) and i > 1:
        p = primes[current_prime]
        if i % p == 0:
            i //= p
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] += 1
        else:
            current_prime += 1
    if current_prime == len(primes):
        primes.append(n)
        return [(n, 1)]
    else:
        return [(factor, factors[factor]) for factor in factors]


def solution047():
    primes = [2]
    distinct_numbers = []
    target = 4
    i = 3

    while len(distinct_numbers) < target:
        factors = get_prime_factors(i, primes)
        if len(factors) == target:
            distinct_numbers.append(i)
        else:
            distinct_numbers = []
        i += 1

    return distinct_numbers[0]
