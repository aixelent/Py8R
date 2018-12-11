def values(num):
    if len(num) == len(set(num)):
        return True
    else:
        return False

print(values([1, 3, 5, 7, 9, 11, 31, 13, 5, 3]))
print(values([1, 3, 5, 7, 9, 11, 31, 13, 15, 23]))