#add implementation
def add(x,y):
    return x+y
#sub Implementation
def subtract(x,y):
    return x-y  #on master
#mul implementation
def multiply(x,y):
    return x*y   # on bug456
#div implementation
def divide(x,y):
    if y==0:
    return divide_by_0_error
    else:
    return x/y
    
 #square implementation
def square(x):
    return x*x