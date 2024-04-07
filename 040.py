def solution040():
    sizes = [10**x for x in range(2, 7)]

    result = 1
    pos = 10
    i = 10

    while sizes:
        if pos + len(str(i)) > sizes[0]:
            print(sizes[0])
            d = int(str(i)[sizes[0] - pos - len(str(i))])
            print(i)
            print(d)
            result *= d
            sizes = sizes[1:]
        pos += len(str(i))
        i += 1
    return result
