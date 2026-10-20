def manhattan(a, b):
    distance = 0

    for x, y in zip(a, b):
        distance += abs(x - y)

    return distance
