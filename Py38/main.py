def find(values):
    min = values[0]

    for val in values:
        if val < min:
            min = val
    return min

print(find([-1, 4, 7, -3, 9, - 11, 14]))
