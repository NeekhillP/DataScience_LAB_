# Print all the prime numbers upto n 

n=int(input("Enter the number upto which you want to print prime numbers"))
if n<2:
    print("Please enter the number greater than 1")

def fact_(n):
    for i in range(2,n+1):
        prime=0
        for j in range (1,i+1):
            if i%j==0:
                prime+=1
        if prime==2:
            print(i)

fact_(n)

    