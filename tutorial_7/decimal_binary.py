num = 10
output = ""

# print(bin(num))
while num > 0:
    output = str(num % 2)+output # 110
    num = num // 2 # quotient
    
print("Binary value is",output)