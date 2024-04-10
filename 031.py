def solution031():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    value = 200

    result = [1]
    for i in range(value):
        result.append(0)

    for i in range(len(coins)):
        for j in range(coins[i], value + 1):
            result[j] += result[j - coins[i]]
    return result[-1]
