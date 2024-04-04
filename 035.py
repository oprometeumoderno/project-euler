from prime import PrimeIterator


def get_rotations(n):
    result = []
    for i in range(len(str(n))):
        result.append(int(f"{str(n)[i:]}{str(n)[0:i]}"))
    return set(result) - {n}


p = PrimeIterator()
primes = set()
current_prime = next(p)
while len(str(current_prime)) < 2:
    current_prime = next(p)

result = 4

while current_prime < 1000000:
    if not set(["2", "4", "6", "8", "0"]).intersection(
        set([x for x in str(current_prime)])
    ):
        primes.add(current_prime)
    current_prime = next(p)

while primes:
    current_prime = primes.pop()
    all_permutations = get_rotations(current_prime)
    if not all_permutations:
        result += 1
    elif all([x in primes for x in all_permutations]):
        result += 1 + len(all_permutations)
        for p in all_permutations:
            primes.remove(p)
print(result)
