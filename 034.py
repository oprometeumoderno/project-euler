import functools
import operator

factorials = [1] + [
    functools.reduce(operator.mul, list(range(1, x + 1))) for x in range(1, 10)
]

result = 0
upper_bound = 10**7
for i in range(10, upper_bound):
    if i == sum([factorials[int(x)] for x in str(i)]):
        result += i

print(result)
