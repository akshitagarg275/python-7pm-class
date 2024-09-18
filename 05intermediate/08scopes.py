# Scopes in Python
'''
It tells us whether a variable/function or lets say any instance
is accessible or not
If it is in the scope than the variable would be accessible
'''
# global scope
a = 10

def fun():
    # local scope
    # a = 20

    # TODO: accessing and modifying global variable
    global a  #It will refer to my global variable
    a = 50
    print("GLOBALS: ",globals()['a'])
    print("Inside fun a: ",a)

# fun()
# print("Outside fun a: ",a)
# print(dir())


def outer():
    b = 20

    def inner():
        nonlocal b
        b = 30
        print("Inner b: ", b)
    inner()
    print("Outer b: ", b)


outer()
