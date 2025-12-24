# Reverse a number using loop (e.g., input 123 → output 321).  

result = 0
num = 1234

while num>0:
    # ld = num % 10 
    # num = num // 10 
    # result = result *10 + ld    

    result = (result *10) + (num % 10) 
    num = num // 10 

print("Rev: ",result)