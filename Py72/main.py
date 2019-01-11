def repeated_char(string):
    temp = {}

    for ch in string:
        if ch in temp:
            return ch
        else:
            temp[ch] = 0

    return None


print(repeated_char("lambda"))
