val = [1, 13, 29, 5, 41, 76, 33, 72, 45, 39, 51, 82, 55, 15, 68, 79, 63, 94, 90, 89, 99]

mod = list(filter(lambda x: (x % 3 == 0) or (x % 5 == 0), val))
print("Numbers: ", mod)
