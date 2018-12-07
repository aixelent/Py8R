import collections
val = [-1, 13, -29, 5, 41, 76, -33, 72, -45, -39, 51, 82, -55, 0, 68, 79, 63, 94, -90, 89, 99]

count = (sum(collections.Counter(val).values()))
print(count)
