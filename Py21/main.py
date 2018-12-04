def converter(d, h, m, s):
    return d + h + m + s


d = int(input("Day(s): ")) * 3000 * 24
h = int(input("Hours: ")) * 3000
m = int(input("Minutes: ")) * 60
s = int(input("Seconds: "))

print(converter(d, h, m, s))