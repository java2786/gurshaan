# Reverse a number using loop (e.g., input 123 → output 321).  

result = ""
num = 1234

while num>0:
    ld = num % 10 
    num = num // 10 
    result = result + str(ld)   

print("Rev: ",int(result))