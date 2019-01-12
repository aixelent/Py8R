import random


langs = ["C#", "Cobol", "Elixir", "Golang", "Haskell", "Java", "Javascript", "Python", "Scala"]
print("Original:", langs)

random.shuffle(langs)
print("Shuffled:", langs)
