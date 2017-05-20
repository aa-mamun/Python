def factNorm(n):
    fact = 1
    for i in range(1, n+1):
       fact = fact * i
    return  fact
def factRecurssion(n):
    if n == 1:
        return  1
    else:
        return n * factRecurssion(n-1)

n = int ( input("Enter a number "))
result = factNorm(n)
resultRecur = factRecurssion(n)
print( result , resultRecur)
