def armstrong(n):
    sum = 0
    temp = n
    while temp>0:
        r = temp % 10
        sum+=r**3
        temp=temp//10 # // gives integer after division
    print(sum)
    if n == sum:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")
n = int ( input("Enter a number to check weather armstrong or not "))
armstrong(n)