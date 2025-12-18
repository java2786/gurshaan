num = int(input("Enter a number: "))

# check if num 3 or 5 or both

#if num % 15 == 0 :
if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")

elif num % 3 ==0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

else:
    print("Invalid")
    

