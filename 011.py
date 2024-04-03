largest = 0
with open('input/011.txt', 'r') as file:
    grid = [
        [int(z) for z in y] for y in
        [x.split(' ') for x in file.read().split("\n")[:-1]]
    ]

    width = len(grid[0])
    height = len(grid)


    # UP AND DOWN
    for i in range(0, height-3):
        for j in range(0, width):
            result = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if result > largest:
                largest = result

    # SIDEWAYS
    for i in range(0, height):
        for j in range(0, width-3):
            result = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if result > largest:
                largest = result

    # DIAGONALLY ASCENDING
    for i in range(3, height):
        for j in range(0, width-3):
            result = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if result > largest:
                largest = result

    # DIAGONALLY DESCENDING
    for i in range(0, height-3):
        for j in range(0, width-3):
            result = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if result > largest:
                largest = result

print(largest)
