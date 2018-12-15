def concat(*args, n=0):
    if n > len(args) or n < 1:
        n = len(args)
    return "! ".join(args[:n])


print(concat("C#", "Cobol", "Golang", "Java", "Javascript", "Scala"))
