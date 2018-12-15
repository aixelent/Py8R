def array_checker(values, v):
    for val in values:
        if v == val:
            return True
        else:
            return False


print(array_checker([-1, 1, 3, 0, 9, 7, 11], -1))
