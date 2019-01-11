from math import pi


def rad_to_deg():
    val= float(input("Radians: "))
    return val * 180/pi


print(rad_to_deg())
