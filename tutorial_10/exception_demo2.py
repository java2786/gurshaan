with open("greet.txt") as fileObj:
    print(fileObj.read())


first_num = int(input("Enter first number: "))  # ValueError -> five
second_num = int(input("Enter second number: ")) # ValueError -> nine

print("Sum:",first_num+second_num)
print("Sub:",first_num-second_num)
print("Mul:",first_num*second_num)
print("Div:",first_num//second_num)         # ZeroDivisionError -> div by 0
