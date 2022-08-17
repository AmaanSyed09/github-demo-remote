#Add implementation
def add(x,y):
   return x+y
#Sub Implementation
def subtract(x,y):
   return x-y  #on bug 456
#Mul implementation
def multiply(x,y):
    return x*y   # on bug456
#Div implementation
def divide(x,y):
    if y==0:
    return divide_by_0_error
    else:
    return x/y
    
#Square implementation
def square(x):
    return x*x