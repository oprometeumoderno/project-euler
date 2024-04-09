from prime import sieve

SIZE = 2000000


def solution010():
    primes = sieve(SIZE)

    return sum(primes)
