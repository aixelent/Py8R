list_one = ["C#", "Cobol", "Elixir", "Golang", "Haskell", "Java", "Javascript", "Python", "Scala"]
list_two = ["C#", "Cobol", "Elixir", "Java", "Javascript", "Python"]

print(list(set(list_one) - set(list_two)))
