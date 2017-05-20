def add(a,b):
    result = a + b
    return result
def sub(a,b):
    result = a - b
    return result
def mul(a,b):
    result = a * b
    return result
def div(a,b):
    result = a / b
    return result

dict ={1:add,2:sub,3:mul,4:div}
x = int ( input("Enter first number "))
y = int ( input("Enter second number "))
z = int ( input("Enter your choice (press 1 or 2 or 3 or 4 ) ---- 1 : ADD , 2 : SUB , 3 : MUL , 4 : DIV "))

print(dict[z](x,y)) #calling function through dictionary

