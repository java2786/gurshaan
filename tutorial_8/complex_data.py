"""
student = 
    name
    contacts - 
        phone - 8789734, 98793933
        email - 2 email 
        address - 
    subject with each subject has score - 
    cgpa score -
    age
"""

# List [] - use for order, access by index
# Set {} - use for unique values
# Tuple () - read only
# Dictionary {} - key:value, label, pair
student = {
    "name": "Ramesh",
    "contact": {
        "phone": [8789734, 98793933],
        "email": ["ramesh@gmail.com", "ram@ymail.com"],
        "address": {
            "permanent": "Delhi",
            "office": "Noida",
            "residential": "Noida"
        }
    },
    "subjects": {
        "math": 76, "physics": 89, "english": 83
    },
    "cgpa_scroe": 0,
    "age": 21
}

print("Name:",student["name"])
print("Subjects:",student["subjects"])

# subjects = student["subjects"]
# for key in (subjects):
#     # print("Key:",key)
#     print(subjects[key])

# for key in (student["subjects"]):
#     print(student["subjects"][key])
total_score = 0
for key,value in (student["subjects"].items()):
    # print(student["subjects"][key]," ",value)
    total_score = total_score + value
    
print("Total Score:",total_score)
student["cgpa_scroe"] = total_score/2

print(student["cgpa_scroe"])