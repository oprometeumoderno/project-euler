with open("input/013.txt", "r") as file:
    total = sum([int(x) for x in file.read().split("\n")[:-1]])
    print(str(total)[0:10])
