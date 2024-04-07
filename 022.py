def solution022():
    with open("input/022.txt", "r") as file:
        names = [x[1:-1] for x in file.read().split(",")]

        names = sorted(names)

        result = 0
        for name in range(0, len(names)):
            score = 0
            for c in names[name]:
                score += ord(c) - ord("A") + 1
            result += score * (name + 1)

    return result
