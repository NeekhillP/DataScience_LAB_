# 1
# Create a text file and write multiple lines into it
# Read the contents of the file and display them on the screen
# Handle the case where the file does not exist using try-except

with open ("qst1.txt", "w") as f:
        f.write("This is the first line.\n")
        f.write("This is the second line.\n")
        f.write("This is the third line.\n")
print("Multiple lines written in file successfully.")

try:
    with open ("qst2.txt", "r") as f:
        contents = f.read()
        print("contents in the file after reading:")
        print(contents) 
    
except FileNotFoundError:
    print("The file does not exist.")