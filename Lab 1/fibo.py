#that will print fibonacci series upto n term 

n=int(input("Enter the number of terms you want in fibonacci series"))

def fib(n):
    if n<=1:
        return n 
    else:
        return fib(n-1)+fib(n-2)


for i in range(n):
    print(fib(i))
