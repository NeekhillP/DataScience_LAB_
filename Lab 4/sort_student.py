# 1. Write a Python script that takes a list of student marks and sorts them in descending
# order (highest to lowest) using either the sorted() function or the .sort() method.

marks = []

def input_marks():
    n = int(input("Enter the number of students:"))
    for i in range(n):
        mark = float(input(f"Enter mark for student {i + 1}: "))
        marks.append(mark)
        
def sort_marks():
    marks.sort(reverse=True)
    print("Sorted marks:", marks)

input_marks()
sort_marks()