import operator
import functools

result =  sum(
    [
        int(x) for x in str(
            functools.reduce(
                operator.mul,
                list(range(1,101))
            ))
    ]
)


print(result)
