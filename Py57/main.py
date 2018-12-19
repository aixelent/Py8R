def longest_word(file):
    with open(file, "r") as f:
        words = f.read().split()

    longest_word = len(max(words, key=len))
    return [word for word in words if len(word) == longest_word]


print(longest_word("/home/xhexe/Py/Py8R/files/text.txt"))
