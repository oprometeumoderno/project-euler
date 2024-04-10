from prime import PrimeIterator


def expand_squares(squares, n):
    while squares[-1] < n:
        squares.append(2 * (len(squares) + 1) ** 2)
    return set(squares)


def expand_primes(primes, n, p):
    while primes[-1] < n:
        primes.append(next(p))
    return set(primes)


def solution046():
    i = 9
    p = PrimeIterator()
    primes = [next(p)]
    squares = [2]

    while True:
        square_set = expand_squares(squares, i)
        prime_set = expand_primes(primes, i, p)
        found = False
        if i not in prime_set:
            for prime in primes:
                if (i - prime) in square_set:
                    found = True
                    break
            if not found:
                return i
        i += 2
