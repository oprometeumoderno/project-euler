from itertools import permutations
from math import floor, sqrt


def is_prime(n):
    for i in range(3, floor(sqrt(n))):
        if n % i == 0:
            return False
    return True


def get_all_pandigital_permutations(max_n):
    all_permutations = []
    for last_digit in [x for x in [1, 3, 7, 9] if x <= max_n]:
        possible_digits = set(list(range(1, max_n + 1)))
        all_permutations.extend(
            [
                "".join(list([str(y) for y in x]) + [str(last_digit)])
                for x in permutations(set(possible_digits) - set([last_digit]))
            ]
        )
    return all_permutations


max_prime = 0
for digits in range(4, 10):
    for permutation in get_all_pandigital_permutations(digits):
        if is_prime(int(permutation)) and int(permutation) > max_prime:
            max_prime = int(permutation)

print(max_prime)
