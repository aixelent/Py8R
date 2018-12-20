from collections import Counter

def word_occurences(file):
    with open(file) as f:
        print("Words statistic: ", Counter(f.read().split()))

word_occurences("/home/xhexe/Py/Py8R/files/text.txt")