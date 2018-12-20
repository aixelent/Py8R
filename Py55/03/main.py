def text_to_list(file):
    flist = []

    with open(file) as f:
        text = f.read().split()
        print(text)


print(text_to_list("/home/xhexe/Py/Py8R/files/text.txt"))
