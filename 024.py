import functools
import operator

TARGET = 1000000 - 1

def nth_permutation(digits, target):
    if len(digits) == 1:
        return str(digits[0])
    possibilities = functools.reduce(
        operator.mul, list(range(1, len(digits)))
    )

    i = int(target // possibilities)
    target = target % (possibilities * i)
    digit = digits[i]
    digits.remove(digit)
    return str(digit) + nth_permutation(digits, target)

print(nth_permutation([x for x in range(0,10)], TARGET))
