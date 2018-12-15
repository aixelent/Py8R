def read_lines(file, lines):
    lines_list = []

    with open(file) as f:
        for i in range(lines):
            lines_list.append(f.readline())
        return lines_list

print(read_lines("/home/xhexe/Py/Py8R/files/text.txt", 4))
