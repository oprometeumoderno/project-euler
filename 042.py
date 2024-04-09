def solution042():
    with open("input/042.txt", "r") as file:
        words = [w[1:-1] for w in file.read().split(",")]
        scores = [sum([ord(c) - ord("A") + 1 for c in word]) for word in words]
        triangle_numbers = set()
        n = 0
        while (n * (n + 1)) // 2 < max(scores):
            triangle_numbers.add((n * (n + 1)) // 2)
            n += 1
        return len([score for score in scores if score in triangle_numbers])
