def multiply(values):
    sum = 1
    for elem in values:
        sum *= elem
    return sum


print(multiply([1, 6, 3]))
print(multiply([2, 2, 2, 2, 2, 1, 2]))
