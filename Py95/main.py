import random

with open("/home/xhexe/Py/Py8R/files/text.txt", ) as file:
    lines = file.readlines()
    print(random.choice(lines))
