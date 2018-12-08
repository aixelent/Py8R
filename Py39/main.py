def find(values):
    max = values[0]

    for val in values:
       if val > max:
           max = val
    return max

print(find([-1, 4, 7, -3, 9, - 11, 14, 8, 88, -88]))
