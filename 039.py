n = 1
max_n = 100
perimeters = {}
while n <= max_n:
    m = n + 1
    max_m = 1000 // n
    while m <= max_m:
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        k = 1
        while k * a + k * b + k * c < 1000:
            perimeter = k * a + k * b + k * c
            if perimeter in perimeters:
                perimeters[perimeter].add((k**3) * a * b * c)
            else:
                perimeters[perimeter] = set({(k**3) * a * b * c})
            k += 1
        m += 1
    n += 1

print(sorted([(x, perimeters[x]) for x in perimeters], key=lambda x: len(x[1]))[-1][0])
