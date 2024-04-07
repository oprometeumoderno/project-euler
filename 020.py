import operator
import functools


def solution020():
    result = sum(
        [int(x) for x in str(functools.reduce(operator.mul, list(range(1, 101))))]
    )
    return result
