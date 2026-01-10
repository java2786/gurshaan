path = "./../task.txt"

with open(path) as file_obj:
    lines = file_obj.readlines()
    for i in range(len(lines)):
        print(lines[i],end="")
        