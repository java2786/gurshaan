a = 433
b = 433
c = 433

# if a>b and a>c:
#     print(a, "is max: A")
# elif b>a and b>c:
#     print(b,"is max: B")
# elif c>a and c>b:
#     print(c,"is max: C")  
# else:
    # if a > b and b==c:
    #     pass 
    # elif b>a and b==c 
    
if a>b:
    # a is greater than b
    if a>c:
        print(f"{a} is max")
    elif a<c:
        print(f"{c} is max") 
    else:
        # a and c are same
        print(f"{a} is max, a and c are same")
elif b>a:
    if b>c:
        print(f"{b} is max")
    elif b<c:
        print(f"{c} is max") 
    else:
        # a and c are same
        print(f"{b} is max, b and c are same")
else:
    print(f"{a} and {b} are same, a and b")