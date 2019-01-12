import random

langs = ["C#", "Cobol", "Elixir", "Golang", "Haskell", "Java", "Javascript", "Python", "Scala"]
sec_random = random.SystemRandom()
print(sec_random.choice(langs))
