def calculate(x, y):
    return (x * y) + (x * y) / 2**3


x = float(input("Enter x: "))
y = float(input("Enter y: "))

if x and y == 0:
    print("0")
else:
    print("Tadam: ", calculate(x, y))
