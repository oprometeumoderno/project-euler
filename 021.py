from math import sqrt, floor


def sum_of_divisors(n):
    if n == 1:
        return 1
    divisors = [1]
    root = sqrt(n)
    for i in range(2, floor(root)):
        if n % i == 0:
            divisors.append(int(n // i))
            divisors.append(i)
    if root == floor(root):
        divisors.append(floor(root))
    return sum(divisors)


def solution021():
    result = 0
    for i in range(1, 10000):
        sod = sum_of_divisors(i)
        if sum_of_divisors(sod) == i and i != sod:
            result += i

    return result
