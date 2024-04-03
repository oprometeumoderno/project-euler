from math import sqrt, floor

LIMIT = 28123



def is_abundant(n):
    divisors = [1]
    root = int(floor(sqrt(n)))
    for i in range(2, root + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n//i))
    if sqrt(n) == root:
        divisors.remove(int(root))
    if sum(divisors) > n:
        return True
    else:
        return False

abundant_numbers = set()
for i in range(1, 28123):
    if is_abundant(i):
        abundant_numbers.add(i)

result = 0
for i in range(1, LIMIT):
    can_be_sum = False
    for abundant_num in abundant_numbers:
        if (i - abundant_num) in abundant_numbers:
            can_be_sum = True
            break
    if not can_be_sum:
        result += i

print(result)
#print(get_sum_divisors(64))
