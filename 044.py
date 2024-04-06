def get_pentagon_number(n):
    return int((n * (3 * n - 1)) / 2)


pentagon_numbers = set()
i = 1
found = False
while not found:
    pentagon = get_pentagon_number(i)
    for p_k in pentagon_numbers:
        p_j = pentagon - p_k
        if p_j in pentagon_numbers and p_k - p_j in pentagon_numbers:
            print(f"{p_k - p_j}")
            found = True
    pentagon_numbers.add(pentagon)
    i += 1
