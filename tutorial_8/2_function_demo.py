"""
def buyItemByCode(code):
    if code==1:
        return "Samosa"
    elif code == 2:
        return "Masala Tea"
    else:
        return "Water"



item = buyItemByCode(1)
item = buyItemByCode(2)
item = buyItemByCode(3)
"""

def add(a, b):
    return a+b 

def mul(a, b):
    return a*b 

print(add(5,8))

def findStd(roll):
    roll = roll 
    name = "Ramesh"
    score = 83
    
    # return [roll, name, score] # list
    return (roll, name, score) # tuple

student = findStd(123)
# student[1] = "Mahesh"
print(student[2])
print(type(student))