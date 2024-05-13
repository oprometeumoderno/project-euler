from prime import sieve


def solution069():
    limit = 1_000_000
    primes = sieve(1000)
    result = 2
    i = 1
    while result * primes[i] < limit:
        result *= primes[i]
        i += 1

    return result
