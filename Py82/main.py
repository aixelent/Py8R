val = [1, 1, 3, 5, 7, 1, 3, 0, 9, 1, 4]
val2 = []

for v in val:
    if v not in val2:
        val2.append(v)
val2.sort()
print(val2)
