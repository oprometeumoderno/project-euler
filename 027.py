from prime import sieve


def solution027():
    max_length = 0
    max_length_coeff = (None, None)
    primes = set(sieve(1000**2 + 1000))
    b = [x for x in primes if x < 1000]
    for a in range(-1000, 1001):
        for prime_number in b:
            n = 0
            length = 0
            while n**2 + a * n + prime_number in primes:
                length += 1
                n += 1
            if length > max_length:
                max_length = length
                max_length_coeff = (a, prime_number)

    return max_length_coeff[0] * max_length_coeff[1]
