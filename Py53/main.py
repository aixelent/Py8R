from itertools import islice

def read_lines(file, lines):
    with(open(file)) as f:
        for lines in islice(f, lines):
            print(lines)

print(read_lines("/home/xhexe/Py/Py8R/files/text.txt", 4))
