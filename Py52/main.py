def fopen(file):
    text = open(file)
    return text.read()
    # print(text.read())

print(fopen("/home/xhexe/Py/Py8R/files/file.txt"))
