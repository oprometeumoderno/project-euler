from prime import PrimeIterator


def solution049():
    p = PrimeIterator()
    primes = dict()
    current_prime = next(p)
    while current_prime < 1000:
        current_prime = next(p)
    while current_prime < 10000:
        index = "".join(sorted([str(s) for s in str(current_prime)]))
        if index not in primes:
            primes[index] = [current_prime]
        else:
            primes[index].append(current_prime)
        current_prime = next(p)

    primes = {index: primes[index] for index in primes if len(primes[index]) >= 3}
    for index in primes:
        while len(primes[index]) >= 3:
            first = primes[index][0]
            for i in range(1, len(primes[index])):
                diff = primes[index][i] - first
                if index != "1478":
                    if primes[index][i] + diff in primes[index]:
                        return int(f"{first}{first + diff}{first + 2 * diff}")
            primes[index] = primes[index][1:]
