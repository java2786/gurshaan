num = 1364578
count = 0

while num>0:
    # num % 10 -> last digit
    lastDigit = num % 10
    count = count + 1
    # num // 10 -> remove last digit
    num = num // 10

print(count)