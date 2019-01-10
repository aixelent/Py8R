def sep_str():
    inp = input(str("Enter word/words with '*' sign wherever you want: ")).rsplit("*", 1)[0]
    return inp


print(sep_str())
