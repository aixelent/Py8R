dict_values = {1: "C#", 2: "Cobol", 3: "Elixir", 4: "Golang", 5: "Haskell", 6: "Java", 7: "Javascript", 8: "Python", 9: "Scala"}
for count, (key, value) in enumerate(dict_values.items(), 1):
    print(key, ' ', value, ' ', count)
