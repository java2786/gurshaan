# description = "thIS iS a ManGO. I liKE tO EAt mANGo."

# This Is A Mango. I Like To Eat Mango.



# description = "thIS iS ManGO."
# description = "thIS iS a ManGO."
description = "thIS iS a ManGO. I liKE tO EAt mANGo."

# print(description.capitalize())

# break all words, break wherever space is found
words = description.split()
print("Total words count: ",len(words))
# ['thIS', 'iS', 'a', 'ManGO.']

# print(words[0]) - 'thIS' -> [2] - I
# print(words[1]) - 'iS' -> [1] - S
# print(words[2]) - 'a'
# print(words[3]) - 'ManGO.'


# print(words[0].capitalize()) 
# print(words[1].capitalize()) 
# print(words[2].capitalize()) 
# print(words[3].capitalize()) 

words[0] = words[0].capitalize() 
words[1] = words[1].capitalize() 
words[2] = words[2].capitalize() 
words[3] = words[3].capitalize() 

print(words)


print(" ".join(words))