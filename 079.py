def solution079():
    succeeding = dict()
    with open("input/079.txt") as file:
        lines = file.read().split("\n")[:-1]
        for line in lines:
            if line[0] not in succeeding:
                succeeding[line[0]] = set()
            if line[1] not in succeeding:
                succeeding[line[1]] = set()
            succeeding[line[0]].add(line[1])
            succeeding[line[0]].add(line[2])
            succeeding[line[1]].add(line[2])
    digits = sorted(
        [(k, sorted(list(succeeding[k]))) for k in succeeding],
        key=lambda x: len(x[1]),
        reverse=True,
    )
    return int("".join([x[0] for x in digits] + list(digits[-1][1])))
