def solution028():
    result = 1
    curr = 1
    size = 1001

    for i in range(0, size * 2 - 2):
        curr += 2 * (i // 4 + 1)
        result += curr

    return result
