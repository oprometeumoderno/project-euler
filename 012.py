import math

def number_of_factors(n):
    is_even = n % 2 == 0
    result = 0
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            result += 2
        if is_even:
            i += 1
        else:
            i += 2
    return result


found = False
i = 2
while not found:
    _sum = (i * (i+1))/2
    if number_of_factors(_sum) > 500:
        found = True
    else:
         i += 1

print(int(_sum))
