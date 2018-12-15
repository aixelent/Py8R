def text_to_array(file):
    array = []

    with open(file) as f:
        for line in f:
            array.append(line)
        print(array)


text_to_array("/home/xhexe/Py/Py8R/files/text.txt")
