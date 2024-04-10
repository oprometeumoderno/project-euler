def solution045():
    n = 166
    m = 3
    hexagonal_number = 0
    while True:
        hexagonal_number = n * (2 * n - 1)
        pentagonal_number = 0
        while (m * (3 * m - 1)) / 2 <= hexagonal_number:
            pentagonal_number = (m * (3 * m - 1)) / 2
            m += 3
        if pentagonal_number == hexagonal_number:
            break
        n += 1
    return int(pentagonal_number)
