last = 1
current = 2
result = 0
while current < 4000000:
    if current % 2 == 0:
        result += current
    next_one = current + last
    last = current
    current = next_one

print(result)
