def pow(n, m):
    output = 1
    for p in range(m):
        output = output * n
    return output 

# print(pow(2,3)) # 8
# print(pow(3,2)) # 9
# print(pow(2,7)) # 128


def binaryToDecimal(b):
    index = 0
    decimal = 0

    while b>0:
        ld = b % 10
        decimal = decimal + pow(2,index) * ld
        index = index+1
        b = b // 10
    return decimal
    
print(binaryToDecimal(110))
print(binaryToDecimal(101))
