import functools
import operator


def solution008():
    largest = 0

    with open("input/008.txt", "r") as file:
        big_number = "".join(file.read().split("\n"))
        for i in range(0, len(big_number) - 11):
            current_mul = functools.reduce(
                operator.mul, list([int(x) for x in big_number[i : i + 13]])
            )
            if current_mul > largest:
                largest = current_mul
    return largest
