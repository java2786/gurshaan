# go to market for shopping

# list -> pen, shampoo, soap, ghee, diary, fruits, milk

# CRUD - Create,Read,Update,Delete

shoppingList = []
print(type(shoppingList))

# adding two items
shoppingList.append("Fruits")
shoppingList.append("Milk")
shoppingList.append("Toys")
shoppingList.append("Pen")
shoppingList.append("Soap")
shoppingList.append("Lassi")

print(shoppingList) # full list

print(shoppingList[0]) # get first element
print(shoppingList[1]) # get second element

print(shoppingList[len(shoppingList)-1]) # get last 
print(shoppingList[-1]) # get last 


shoppingList[-1] = "Sweet Lassi"

print(shoppingList[-1]) # get last 


shoppingList.remove("Pen")
print(shoppingList) # print whole list 
