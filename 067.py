def solution067():
    with open("input/067.txt", "r") as file:
        lines = file.read().split("\n")[:-1]
        triangle = [[int(x) for x in line.split(" ")] for line in lines][::-1]

        for line in range(1, len(triangle)):
            for row in range(0, len(triangle[line])):
                possibilities = [triangle[line - 1][row], triangle[line - 1][row + 1]]
                triangle[line][row] += max(possibilities)
        return triangle[-1][0]
