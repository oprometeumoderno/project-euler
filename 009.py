n = 1
max_m = 20
max_n = 20
found = False
while not found and n <= max_n:
    m = n
    while not found and m <= max_m:
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        k = 0
        while k * a + k * b + k * c < 1000:
            if a + b + c == 1000:
                print(f"{a*b*c}")
                found = True
            k += 1
        m += 1
    n += 1
