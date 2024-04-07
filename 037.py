from prime import PrimeIterator


def get_all_truncated_primes(p):
    truncated_primes = set([p])
    truncated_primes.update([int(str(p)[i:]) for i in range(1, len(str(p)))])
    truncated_primes.update([int(str(p)[:-i]) for i in range(1, len(str(p)))])

    return truncated_primes


def solution037():
    p = PrimeIterator()
    current_prime = next(p)
    primes = set()
    while current_prime < 10:
        primes.add(current_prime)
        current_prime = next(p)

    result = 0
    found = 0
    while found < 11:
        current_prime = next(p)
        primes.add(current_prime)
        if (
            not set([c for c in "02468"]).intersection(
                [c for c in str(current_prime)[1:]]
            )
            and str(current_prime)[0] not in ["1", "4", "6", "8"]
            and str(current_prime)[-1] != "1"
        ):
            if all([x in primes for x in get_all_truncated_primes(current_prime)]):
                found += 1
                result += current_prime

    return result
