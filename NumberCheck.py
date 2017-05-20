n = int (input("Enter the limit "))

for i in range(2,n):
    isPrime = True
    for j in range(2,i):
        if i % j == 0 :
            isPrime = False
    if isPrime :
        print(i,end=" ")