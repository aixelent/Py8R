def temp_converter():
    temp = input("Enter temperature (e.g. 77C or 111F):").upper()
    degree = int(temp[:-1])
    conv = temp[-1]

    if conv.upper() == "F":
        result = int(round(degree - 32) * 5 / 9)
        oconv = "Fahrenheit"
    elif conv.upper() == "C":
        result = int(round(9 * degree) / 5 + 32)
        oconv = "Celsius"
    else:
        quit()
    print(temp, "is", result, "degrees.")


temp_converter()
