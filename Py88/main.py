def greater_than(values, val):
    return [v for v in values if v >= val]


print(greater_than([1, 8, 12, 3, 5, 31, 34, 35], 30))
print(greater_than([1, 8, 12, 3, 5, 31, 34, 35], 10))
