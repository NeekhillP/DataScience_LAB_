n=int(input("Enter the year "))

def leap(n):
    if (n%4==0 and n%100!=0 ) or  n%400==0:
        print(f"the given year {n} is leap year")
    
    else:
        print(f"The given year {n} is not a leap year")
    
leap(n)             