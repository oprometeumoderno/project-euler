def get_digits(n):
    return "".join(sorted(str(n)))


def solution052():
    x = 1
    while True:
        digits_x = get_digits(x)
        if (
            digits_x == get_digits(2 * x)
            and digits_x == get_digits(3 * x)
            and digits_x == get_digits(4 * x)
            and digits_x == get_digits(5 * x)
            and digits_x == get_digits(6 * x)
        ):
            return x
        x += 1
