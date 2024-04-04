upper_bound = 10**6
result = 0
for i in range(1, upper_bound):
    if str(i) == str(i)[::-1] and f"{i:b}" == f"{i:b}"[::-1]:
        result += i

print(result)
