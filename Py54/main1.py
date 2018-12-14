def append_text(file):
    with open(file, "a") as f:
        f.write("\nAppend me!")
        text = open(file)
    return text.read()

print(append_text("/home/xhexe/Py/Py8R/files/text.txt"))
