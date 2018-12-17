def text_to_list(file):
    with open(file) as f:
        text = f.readlines()
        print(text)


print(text_to_list("/home/xhexe/Py/Py8R/files/text.txt"))
