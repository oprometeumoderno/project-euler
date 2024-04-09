import math
import functools
import operator


class PrimeIterator:
    def __init__(self):

        self.primes = []
        self.n = 2

    def newton_root(self, n):
        tolerance = 0.5
        x = n / 2
        while True:
            root = 0.5 * (x + (n / x))
            if abs(root - x) < tolerance:
                break
            x = root
        return root

    def __next__(self):
        if not self.primes:
            self.primes.append(self.n)
            self.n = 3
            return self.primes[-1]
        else:
            i = 0
            while self.primes[i] < self.newton_root(self.n):
                if self.n % self.primes[i] == 0:
                    i = 0
                    self.n += 2
                else:
                    i += 1
            self.primes.append(self.n)
            self.n += 2
            return self.primes[-1]


def prime_division(n):
    p = PrimeIterator()
    result = []
    while n != 1:
        current_prime = next(p)
        if n % current_prime == 0:
            n = n // current_prime
            result.append((current_prime, 1))
            while n % current_prime == 0:
                n = n // current_prime
                result[-1] = (current_prime, result[-1][1] + 1)
    return result


def is_prime(n):
    for i in range(3, math.floor(math.isqrt(n))):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    divs_a = dict(prime_division(a))
    divs_b = dict(prime_division(b))

    gcd = {}
    for divisor in divs_a:
        if divisor in divs_b:
            gcd[divisor] = min([divs_a[divisor], divs_b[divisor]])
    return functools.reduce(operator.mul, [x ** gcd[x] for x in gcd])
