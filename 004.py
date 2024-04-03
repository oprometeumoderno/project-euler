largest = 0
for x in range(100, 1000):
    for y in range(x, 1000):
        if str(x * y) == str(x * y)[::-1] and x * y > largest:
            largest = x * y

print(largest)
