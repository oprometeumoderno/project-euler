def invert_fraction(numerator, denominator):
    aux = numerator
    numerator = denominator
    denominator = aux
    return numerator, denominator


def solution065():
    nth_convergence = 100
    e_sequence = [1, 2]

    for current_convergence in range(len(e_sequence), nth_convergence - 1):
        if current_convergence % 3 != 1:
            e_sequence.append(1)
        else:
            e_sequence.append(2 * (1 + (current_convergence // 3)))

    numerator = 1
    denominator = e_sequence[-1]
    del e_sequence[-1]
    while len(e_sequence) > 0:
        numerator += denominator * e_sequence[-1]
        del e_sequence[-1]
        numerator, denominator = invert_fraction(numerator, denominator)

    numerator = denominator * 2 + numerator
    return sum([int(d) for d in str(numerator)])
