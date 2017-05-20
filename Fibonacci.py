def fibonacci(n):
    first = 0
    second=1
    next =0
    for i in range(0,n):
        if i <= 1 :
            next = i
        else:
            next = first + second
            first = second
            second = next
        print(" ",next)

def fibonacciRecurssion(n):
    if n<=1:
        return n
    else:
        return ( fibonacciRecurssion(n-1) + fibonacciRecurssion(n-2) )
n = int(input("Enter the limit"))
fibonacci(n)

for i in range(n):
    print(fibonacciRecurssion(i),end=" ")


