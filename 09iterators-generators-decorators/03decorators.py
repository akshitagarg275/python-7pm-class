# TODO: decorators

'''
It allows us to modify the behaviour of a function or class
First class objects: Functions are first class objects, which means
that functions can be passed as an argument
'''


def upper(text):
    return text.upper()

# print(upper("python"))
res = upper
# print(res)
# print(res("programming"))

# TODO: passing the function as an argument

def lower(text):
    return text.lower()

def greet(fn):
    greeting = fn("PYTHON PROGRAMMING")
    print(greeting)

# greet(lower)

# TODO: returning a function

def create_adder(num1):
    def adder(num2):
        return num1 + num2
    
    return adder

# res = create_adder(5)
# print(res(4))

# TODO: decorator
def outer_decorator(func):
    def inner1():
        print("**************")
        func()
        print("**************")
    return inner1

@outer_decorator
def actual_fun():
    print("I am inside actual function")

# res = outer_decorator(actual_fun)
# res()

# actual_fun()
