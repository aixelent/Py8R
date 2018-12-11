def values(num):
    return False if len(num) > len(set(num)) else True

print(values([1, 3, 5, 7, 9, 11, 31, 13, 5, 3]))
print(values([1, 3, 5, 7, 9, 11, 31, 13, 15, 23]))
