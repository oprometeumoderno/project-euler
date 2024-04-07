from prime import PrimeIterator


def solution007():
    p = PrimeIterator()

    return [next(p) for _ in range(1, 10002)][-1]
