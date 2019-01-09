def char_replace():
    inp = input("Enter a word(s): ")
    return inp[0] + inp.replace(inp[0], 'x')[1:]


print(char_replace())
