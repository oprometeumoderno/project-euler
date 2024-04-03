from prime import PrimeIterator

p = PrimeIterator()

print([next(p) for _ in range(1, 10002)][-1])
