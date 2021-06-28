# normal function to add two numbers
def func(a,b):
    s=a+b
    return s
print("Sum is",func(5,6))#Sum is 11
#print("Sum is",func(5,6,7))#TypeError: func() takes 2 positional arguments but 3 were given
#function with variable length arguments(using *) to add 0 or more values
def func1(*b):
    s=0
    for i in b:
        s+=i
    return s
print("Sum is",func1(5,6,7))#Sum is 18
#finding type of variable length argument
def func1(*b):
    s=0
    print(type(b))#<class 'tuple'>
    for i in b:
        s+=i
    return s
print("Sum is",func1(5,6,7))
"""
a,The variable length arguments if present in the function definition should be
last in the list of parameters.
b,Inside the called function, for loop is used to access the arguments.
c,The arbitrary number of arguments passed to the function forms a
tuple before being passed into the function.
"""
