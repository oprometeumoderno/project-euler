from prime import PrimeIterator

max_length = 0
max_length_coeff = (None, None)
primes = set()
p = PrimeIterator()
current_prime = next(p)
while current_prime < 1000**2 + 1000:
    primes.add(current_prime)
    current_prime = next(p)

for a in range(-1000, 1001):
    b = [x for x in primes if x < 1000]
    for prime_number in b:
        n = 0
        length = 0
        while n**2 + a * n + prime_number in primes:
            length += 1
            n += 1
        if length > max_length:
            max_length = length
            max_length_coeff = (a, prime_number)

print(f"{max_length_coeff[0] * max_length_coeff[1]}")
