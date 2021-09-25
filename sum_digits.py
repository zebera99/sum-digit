def sum_digit(num):
    total = 0
    str_num = str(num)

    for digit in str_num:
        total += int(digit)

    return total


# This is for finding out what the sum is of from adding sum_digit(1) to sum_digit(1000) 
i = 1
range = 0
while i <= 1000:
    range += sum_digit(i)
    i += 1

print(range)
