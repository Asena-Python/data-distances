def manhattan(a, b):
    return minkowski(a, b, 1)


def euclidean(a, b):
    return minkowski(a, b, 2)


def minkowski(a, b, p):
    distance = 0

    for x, y in zip(a, b):
        distance += abs(x - y) ** p

    return distance ** (1 / p)