def num_occurences(values):
    count = 0

    for val in values:
        if val == 0:
            count += 1

    return count


print(num_occurences([0, 1, 7, 5, 0, 2, 4, 0, 9, 0]))
