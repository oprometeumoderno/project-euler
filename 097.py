def solution097():
    n = 1
    for i in range(7830457):
        n *= 2
        if n > 10**12:
            n = n % 10**11

    return (n * 28433 + 1) % 10**10
