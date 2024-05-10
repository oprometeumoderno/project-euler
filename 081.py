def solution081():
    with open("input/081.txt") as file:
        lines = file.read().split("\n")[:-1]

        matrix = [[int(n) for n in line.split(",")] for line in lines]

        max_w = len(matrix[0]) - 1
        max_d = len(matrix) - 1

        for i in range(max_d, -1, -1):
            for j in range(max_w, -1, -1):
                if j != max_w:
                    if i == max_d:
                        matrix[i][j] += matrix[i][j + 1]
                    else:
                        matrix[i][j] += min(matrix[i][j + 1], matrix[i + 1][j])
                elif i != max_d:
                    matrix[i][j] += matrix[i + 1][j]

        return matrix[0][0]
