def solution048():
    result = 0
    for i in range(1, 1001):
        result += (i**i) % 10**10
    return result % 10**10
