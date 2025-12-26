# find if given number is prime

num = 17
is_prime = True

for d in range(2,num):
    if num%d == 0:
        print(num,"is not prime",d)
        is_prime = False
        break
    
if is_prime == True:
    print(num,"is prime")
else: 
    print(num,"is not prime")