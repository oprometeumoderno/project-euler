from prime import sieve


def solution050():
    primes = sieve(1000000)
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
