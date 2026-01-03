# 4. Write a Python script that takes a list of six student names and uses the
# random.sample() function to randomly select exactly three "Volunteers" for a
# presentation, ensuring that no student is picked more than once in the selection.

import random
student_name = []

def add_names():
    for i in range(6):
        name = input("Enter student name: ")
        student_name.append(name)

def select():
    selected_students = random.sample(student_name, 3)
    print("Selected Volunteers:", selected_students)

add_names()
select()