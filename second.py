# Program to check the number of students and divide them into categories

def categorize_students(num_students):
    if num_students <= 0:
        return "No students to categorize."
    elif num_students <= 10:
        return "Small group"
    elif num_students <= 30:
        return "Medium group"
    elif num_students <= 100:
        return "Large group"
    else:
        return "Very large group"

try:
    num = int(input("Enter the number of students: "))
    category = categorize_students(num)
    print(f"Category: {category}")
except ValueError:
    print("Please enter a valid integer.")