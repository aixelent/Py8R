def sum_digits(val):
    total = 0
    while(val > 0):
        digit_sum = sum([int(st) for st in str(val)])
        val -= digit_sum
        total += 1
    return total


print("Steps to reach zero:", sum_digits(58))
