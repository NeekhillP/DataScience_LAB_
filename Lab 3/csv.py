# 3. CSV File Handling
#  Read data from a CSV file containing student records (roll number, name, marks)
#  Display all student records
#  Handle file-related and data conversion errors using try-except

with open("qst3.csv", "w") as f:
    f.write("Roll No, Name, Marks\n")
    f.write("1, Nikhil, 85\n")
    f.write("2, Mandip, 90\n")
    f.write("3, Bikram, 78\n")
print("written successfully.")

try:
    with open("qst3.csv", "r") as f:
        print("Student Records:")
        for line in f.readlines():
            try:
                roll_no, name, marks = line.strip().split(", ")
                roll_no = int(roll_no)
                marks = float(marks)
                print(f"Roll No: {roll_no}, Name: {name}, Marks: {marks}")
            except ValueError:
                print(f"Skipping invalid record: {line.strip()}")


except FileNotFoundError:
    print("File not found.")