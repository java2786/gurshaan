# 1. Define the student dictionary
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
    "courses": {
        "math": 76,
        "physics": 89,
        "english": 83
    },
    "cgpa_score": 0.0,
    "age": 21
}

# 2. Function to calculate CGPA
def calculate_cgpa(courses):
    total = sum(courses.values())
    return total / len(courses)

# 3. Function to add/update a course
def add_course(courses, course, grade):
    courses[course] = grade

# 4. Function to display student info
def display_student_info(student):
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"CGPA: {student['cgpa_score']:.2f}")
    print("Contact Details:")
    print(f"  Phone: {', '.join(map(str, student['contact']['phone']))}")
    print(f"  Email: {', '.join(student['contact']['email'])}")
    print(f"  Address: {student['contact']['address']}")

# 5. Function to find highest grade
def find_highest_grade(courses):
    highest_course = max(courses, key=courses.get)
    return highest_course, courses[highest_course]

# Example usage
student['cgpa_score'] = calculate_cgpa(student['courses'])
display_student_info(student)
highest_course, highest_grade = find_highest_grade(student['courses'])
print(f"Highest Grade: {highest_course} - {highest_grade}")
