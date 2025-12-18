age = int(input("Enter your age: "))

print(f"Your age is {age}")

# License - valid => 18, 75

# if(age>18):
#     if(age<75):
#         print("Can apply for license")
#     else: 
#         print("Invalid: Senior Citizen")        

# else: 
#     print("Invalid: Minor")
    
# if(age>=18 and age<=75):
#     print("Can apply for license")
# else: 
#     print("Invalid")

if(age<18 or age>75):
    print("Invalid")
else: 
    print("Can apply for license")

