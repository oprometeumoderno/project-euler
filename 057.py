def invert_fraction(numerator, denominator):
    aux = numerator
    numerator = denominator
    denominator = aux
    return numerator, denominator


def solution057():
    numerator = 1
    denominator = 2
    current_iteration = 2
    result = 0
    while current_iteration <= 1000:
        numerator += 2 * denominator
        numerator, denominator = invert_fraction(numerator, denominator)
        if len(str(numerator + denominator)) > len(str(denominator)):
            result += 1
        current_iteration += 1
    return result
