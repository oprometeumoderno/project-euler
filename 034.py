from numba import jit


@jit(nopython=True)
def factorial_sum(n, factorials):
    s = 0
    while n > 0:
        s += factorials[n % 10]
        n //= 10
    return s


@jit(nopython=True)
def solution034():
    factorials = [1, 1]
    for i in range(2, 10):
        factorials.append(i * factorials[-1])

    result = 0
    upper_bound = 10**7
    for i in range(10, upper_bound):
        if i == factorial_sum(i, factorials):
            result += i

    return result
