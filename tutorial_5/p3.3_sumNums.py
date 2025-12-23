# Sum of all odd numbers from 1 to n
sum = 0
n = int(input("Enter a number: "))

for i in range(1,n+1):
    if i % 2 != 0:
        sum = sum + i    
    
print(sum)
