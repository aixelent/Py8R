def repeated_char(sstring):
    hash = {}

    for ch in sstring:
        if ch in hash:
            return ch
        else:
            hash[ch] = 0

    return None


print(repeated_char("lambda"))
