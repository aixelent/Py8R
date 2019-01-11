def digits_in_string(string):
    dig_sum = 0

    for d in string:
        if d.isdigit():
            num = int(d)
            dig_sum += num

    return dig_sum


print(digits_in_string("12345"))
print(digits_in_string("ausd34sg"))
print(digits_in_string("g014ng"))
