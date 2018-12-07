list_of_values = [1, 3, 5, 4, 7, 1, 9, 5, 3]

print("All values less than 10?: ", all(v < 10 for v in list_of_values))
print("All values bigger than 5?:", all(v > 5 for v in list_of_values))
