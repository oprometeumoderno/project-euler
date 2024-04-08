from prime import PrimeIterator

SIZE = 2000000


def solution010():
    sieve = [True] * SIZE
    sieve[0] = False

    for n in range(2, SIZE // 2 + 1):
        m = 2
        while (n * m) <= len(sieve):
            sieve[m * n - 1] = False
            m += 1

    result = 0
    for i in range(len(sieve)):
        if sieve[i]:
            result += i + 1
    return result
