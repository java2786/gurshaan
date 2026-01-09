try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("Welcome",name,"your age is",age)
except ValueError as ve:
    print("Some error occurred")
