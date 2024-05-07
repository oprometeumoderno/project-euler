def solution063():
    result = 0
    for a in range(1, 10):
        for b in range(1, 22):
            if len(str(a**b)) == b:
                result += 1
    return result
