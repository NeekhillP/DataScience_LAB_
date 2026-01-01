num1=input("Enter the first number: ")
num2=input("Enter the second number: ")



if '.' in num1:
    num1 = float(num1)
else:
    num1 = int(num1)

if '.' in num2:
    num2=float(num2)
else:
    num2=int(num2)

result=num1+num2

print("The sum of the numbers is",result)

