with open("/home/xhexe/Py/Py8R/files/text.txt", "a") as f:
    f.write("\nAppend me!")
    text = open("/home/xhexe/Py/Py8R/files/text.txt")
    print(text.read())
