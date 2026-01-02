a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(b>a):
    # swap
    c = a 
    a = b 
    b = c 

# a is greater than b

while True:
    rem = a%b 
    if(rem==0):
        print(b,"is GCD")
        break
    else:
        a = b 
        b = rem 
