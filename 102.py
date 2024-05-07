def contains_origin(p_x, p_y):
    for i in range(0, 3):
        for j in range(i + 1, 3):
            points = [0, 1, 2]
            points.remove(i)
            points.remove(j)
            remaining_point = points[0]
            d_x = p_x[j] - p_x[i]
            d_y = p_y[j] - p_y[i]

            if d_x != 0:
                b = p_y[i] - (p_x[i] * d_y) / d_x
                y = (p_x[remaining_point] * d_y) / d_x + b

                if (p_y[remaining_point] >= y and 0 < b) or (
                    p_y[remaining_point] <= y and 0 > b
                ):
                    return False
            else:
                if p_x[remaining_point] * p_x[i] > 0:
                    return False
    return True


def solution102():
    result = 0
    with open("input/102.txt") as file:
        lines = [x.split(",") for x in file.read().split("\n")[:-1]]
        for line in lines:
            p_x = [int(line[2 * i]) for i in range(0, 3)]
            p_y = [int(line[2 * i + 1]) for i in range(0, 3)]
            if contains_origin(p_x, p_y):
                result += 1
    return result
