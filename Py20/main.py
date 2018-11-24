def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def div(a, b):
    return a / b


print("Choose operation:")
print("1. Add \n2. Subtract \n3. Multiply \n4. Divide")

operation = input("Your choice (1 - 4):")

a = int(input("First value:"))
b = int(input("Second value:"))

if operation == "1":
    print("Add:", add(a, b))
elif operation == "2":
    print("Subtract:", sub(a, b))
elif operation == "3":
    print("Multiply:", multiply(a, b))
elif operation == "4":
    print("Divide:", div(a, b))
else:
    print("Other values isn't a good choice...")

print("end.")