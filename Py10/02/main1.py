x = float(input("Enter x: "))
y = float(input("Enter y: "))

doMath = (x * y) + (x * y) / 2**3

if x and y == 0:
    print("0")
else:
    print("Result: ", doMath)
