def minn(values):
    min = values[0]
    for x in values:
        if x < min:
            min = x
    return min


def maxx(values):
    max = values[0]
    for x in values:
        if x > max:
            max = x
    return max


print(minn([1, 0, 3, 15]))
print(maxx([6, 2, 8, 16]))
