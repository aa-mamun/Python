def armstrong(n):
    sum = 0
    temp = n
    while temp>0:
        r = temp % 10
        sum+=r**3
        temp=temp//10 # // gives integer after division

    if sum == n:
        return sum
    else:
        return 0

n = int ( input("Enter the limit "))
for i in range(1,n+1):
    result = armstrong(i)
    if result != 0:
        print(result)

