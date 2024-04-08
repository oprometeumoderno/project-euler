from prime import PrimeIterator

p = PrimeIterator()


# TODO: move this somewhere else
def generate_primes_sieve(max_prime):
    sieve = [True] * max_prime
    sieve[0] = False

    for n in range(2, max_prime // 2 + 1):
        if sieve[n - 1]:
            m = 2
            while (n * m) <= len(sieve):
                sieve[m * n - 1] = False
                m += 1

    result = []

    for i in range(len(sieve)):
        if sieve[i]:
            result.append(i + 1)
    return result


def solution050():
    primes = generate_primes_sieve(1000000)
    prime_set = set(primes)
    max_length = 0
    max_sum = 0
    for i in range(len(primes)):
        sum = primes[i]
        for j in range(i + 1, len(primes)):
            sum += primes[j]
            if sum > 1000000:
                break
            if sum in prime_set and j - i + 1 > max_length:
                max_sum = sum
                max_length = j - i + 1
    return max_sum
