def char_replace():
    s = input("Enter word:")
    return s[-1:] + s[1:-1] + s[:1]


print(char_replace())
