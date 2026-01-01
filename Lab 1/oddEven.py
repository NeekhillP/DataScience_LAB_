# Write a program that checks if a given number is even or odd.

n=float(input("ENTER THE NUMBER"))
def oddEven(n):
    if n<0:
        print("Entet the number greater than 0")
    elif n%2==0:
        print(f"The number {n} is even")
    else:
        print(f"The number {n} is odd")

oddEven(n)