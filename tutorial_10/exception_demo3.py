try:
    lines = None
    with open("greet.txt") as fileObj:
        lines = fileObj.readlines()
        print(lines)

    print(lines[0])
    first_num = int(lines[1])  
    second_num = int(lines[2]) 
    third_num = int(lines[3]) 

    print("Sum:",first_num+second_num)
    print("Sub:",first_num-second_num)
    print("Mul:",first_num*second_num)
    print("Div:",first_num//second_num)         # ZeroDivisionError -> div by 0
except FileNotFoundError:
    print("File does not exist")
except ValueError:
    print("Input is not correct")
except ZeroDivisionError:
    print("Can not divide by zero")