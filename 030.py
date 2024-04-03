result = 0
for i in range(10, 999999):
    if i == sum([int(x) ** 5 for x in str(i)]):
        result += i
print(result)
