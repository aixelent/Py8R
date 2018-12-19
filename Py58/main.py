def lines_in_file(file):
    with open(file, "rb") as f:
        return len(tuple(f))


print(lines_in_file("/home/xhexe/Py/Py8R/files/text.txt"))
