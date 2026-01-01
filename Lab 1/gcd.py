# Define a function that takes two numbers as arguments, and returns their gcd
n1=int(input("Enter the number"))
n2=int(input("Enter the number"))

def gcd_(n1,n2):
    gcd=1
    for i in range(1,min(n1,n2)+1):
        # print(i)
        if n1%i==0 and n2%i==0:
            gcd=i

    return gcd
print(gcd_(n1,n2))