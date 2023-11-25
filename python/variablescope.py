###########################

print("explaination of Scope of variables")

a=10
def sov():
    a=5
    print('value of variable inside the function - ', a)

sov()
print('value of variable outside function - ', a)

#############################################

print("changing the value of a global variable")

a=10
print("value of a as global variable" , a)
def scopeofvariable():
    global a ##caling global variable
    a=5 ##changing the value of global variable
    print("value of global variable after changed", a)
scopeofvariable()
print("global variable value has changed -" , a)


#############################################
print("how to assign value of a global variable to a local variable inside a function")
a=10
print("value of a global variable" , a)
def variablechange():
    x=globals()["a"]
    print("the value of x is " , x)
variablechange()

