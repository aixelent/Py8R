def two_bjects_sum(x, y):
    if type(x) == type(y) == int:
        return x + y


print(two_bjects_sum(1, 3))
print(two_bjects_sum(3, "a"))
print(two_bjects_sum(3, 1.3))
print(two_bjects_sum(6, 1))