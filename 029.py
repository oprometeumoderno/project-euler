def solution029():
    result = set()

    for a in range(2, 101):
        for b in range(2, 101):
            result.add(a**b)

    return len(result)
