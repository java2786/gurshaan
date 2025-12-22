description = "thIS iS ManGO."
# description = "thIS iS a ManGO."
# description = "thIS iS a ManGO. I liKE tO EAt mANGo."

words = description.split()
print("Total words count: ",len(words))

for i in range(len(words)):
    words[i] = words[i].capitalize() 

print(words)

print(" ".join(words))