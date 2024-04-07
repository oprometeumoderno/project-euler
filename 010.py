from prime import PrimeIterator


def solution010():
    p = PrimeIterator()
    current = next(p)
    sum = 0
    while current < 2000000:
        sum += current
        current = next(p)
    return sum
