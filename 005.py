from prime import PrimeIterator


def divide_if_divisor(n, prime):
    if n % prime == 0:
        return n // prime
    else:
        return n


divisor_list = list(range(2, 21))
p = PrimeIterator()
result = 1

while divisor_list != [1] * len(divisor_list):
    prime = next(p)
    power = 0
    while any([x % prime == 0 for x in divisor_list]):
        divisor_list = [divide_if_divisor(x, prime) for x in divisor_list]
        power += 1
    result *= prime**power
print(result)
