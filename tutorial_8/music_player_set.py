# music_list = {
#     "Jab koi muskil", 
#     "Baby", 
#     "Jai ho",
#     "Jab koi muskil", 
#     "Baby", 
#     "Jai ho"
# }
# print("Type:",type(music_list))
# print("Len:",len(music_list))
# # music_list[4] = "Ice cream"
# print(music_list)


maths_std = {"Ramesh", "Suresh", "Mahesh", "Dinesh", "Ramesh", "Suresh"}
physics_std = {"Suresh", "Mukesh", "Mahesh", "Hitesh", "Mukesh", "Mahesh"}

all_stds = maths_std.union(physics_std)
print(type(all_stds))
print(all_stds)

print("++++++++++++++")
print(maths_std) # {'Ramesh', 'Dinesh', 'Mahesh', 'Suresh'}

