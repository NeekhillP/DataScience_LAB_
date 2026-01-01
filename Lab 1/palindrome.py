## Write a program to check if a given string is palindrome 

str=input("Enter the string").lower()
reverse_str=""
for char in str:
    # print(char)
    reverse_str=char+reverse_str    
def palindrome_(str,r_str):
    if str==reverse_str:
        print(f"The given {str} is palindrome")
    else:
        print("Not palindrome")

palindrome_(str,reverse_str)
    
    

