from math import log as ln


def solution099():
    with open("input/099.txt") as file:
        lines = [
            (int(x[0]), int(x[1]))
            for x in [line.split(",") for line in file.read().split("\n")[:-1]]
        ]
        biggest = 0
        for i in range(1, len(lines)):
            if lines[i][1] * ln(lines[i][0]) > lines[biggest][1] * ln(
                lines[biggest][0]
            ):
                biggest = i
        return biggest + 1  # index to line number
