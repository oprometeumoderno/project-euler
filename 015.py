import functools
import operator

numerator = functools.reduce(operator.mul, list(range(21, 41)))
denominator = functools.reduce(operator.mul, list(range(1,21)))

print(int(numerator/denominator))
