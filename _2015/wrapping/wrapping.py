import math
import operator

def openInput(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            yield line.strip()

def paperArea(dims):
    # print(dims)
    # print(dims[1:] + dims[:1])
    sides = list(map(operator.mul, dims, dims[1:] + dims[:1]))
    return min(sides) + 2 * sum(sides)

def ribbonLength(dims):
    circumference = 2 * (sum(dims) - max(dims))
    volume = math.prod(dims)
    return circumference + volume

def surfaceArea(dims):
    l, w, h = dims
    return 2 * (l * w + l * h + h * w)

def areas(fileName):
    for line in openInput(fileName):
        dimensions = [int(dim) for dim in line.split('x')]
        yield paperArea(dimensions)

def ribbons(fileName):
    for line in openInput(fileName):
        dimensions = [int(dim) for dim in line.split('x')]
        yield ribbonLength(dimensions)

