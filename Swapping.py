a  = int ( input() )
b  = int ( input() )
print("Before swapping " ,a ,b)
'''''
temp = a
a = b
b = temp

a^=b
b^=a
a^=b
'''
a=a+b
b=a-b
a=a-b

print("After swapping" ,a,b)

s1 = "Hello"
s2 = "world"
s1 = s1 + s2
s2 = s1[0 : len(s1) - len(s2)]
s1 = s1[len(s2) : len(s1)]
print(s1 + " " +s2)
