"""
Create student marks list 
- find max score 
- find min score 
- find sum of all
- find average
- max score is 150, create new list with percentage
""" 

marks = [76, 21, 83, 95, 72]
marks.append(94)
print("Marks:",marks)
max = marks[0]
min = marks[0]
avg = 0
sum = 0
percentages = []

for i in range(len(marks)):
    # print(marks[i])
    if(marks[i]>max):
        max = marks[i]
    if(marks[i]<min):
        min = marks[i]
    sum = sum + marks[i]
    
    percentages.append(marks[i] * 100 / 150)
    
print("Max:",max)
print("Min:",min)
print("Sum:",sum)
print("Average:",sum/len(marks))
print("Percents:",percentages)


