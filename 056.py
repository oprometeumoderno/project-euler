def solution056():
    max_digit_sum = 0
    for a in range(100):
        for b in range(100):
            digit_sum = sum(int(d) for d in str(a**b))
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
    return max_digit_sum
