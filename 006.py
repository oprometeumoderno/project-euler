def solution006():
    square_of_sum = sum(list(range(1, 101))) ** 2
    sum_of_square = sum([x**2 for x in list(range(1, 101))])

    return square_of_sum - sum_of_square
