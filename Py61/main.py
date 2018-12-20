import random

def random_line(file):
    with open(file) as f:
        rand = f.read().splitlines()
        print(random.choice(rand))


random_line("/home/xhexe/Py/Py8R/files/text.txt")
