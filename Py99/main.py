def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


option = input("Choose option from 1 - 4:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")

a = int(input("FIrst number:"))
b = int(input("Second number:"))


if option == '1':
    print(add(a, b))
elif option == '2':
    print(subtract(a, b))
elif option == '3':
    print(multiply(a, b))
elif option == '4':
    print(divide(a, b))
else:
    print("Invalid operation")
