# TODO: Functions
'''
we wrap certain lines of code within a function name
so that we can reuse it just by making a function call

def function_name():
    //function statements

'''
# function defination
def greet():
    print("Good morning!")

# function calling
# greet()
# greet()

def greet_name(name):
    print(f"Good Day! {name}")

# greet_name("John")
# n = "Sam"
# greet_name(n)

def add(n1, n2):
    return n1 + n2

# res = add(5,3)
# print(f"res is: {res}")
# print(add(2,3))

# TODO: default parameter
def profile(name, age="NA"):
    print(f"Name is :{name} and age is: {age}")

# profile("Jon", 23)
# n = "Jane"
# profile(n)

def profile2(name="NA", age="NA"):
    print(f"Name is: {name} and age is: {age}")

# profile2()


# TODO: positional arguments

def profile3(name, age):
    print(f"Name is: {name} and age is: {age}")

# profile3(age=24, name="John")

# TODO: varibale length arguments
def func(n1, n2,*args):
    # print("type of args: ", type(args))
    # print("args: ", args)
    print("n1: ", n1)
    print("n2: ", n2)
    for i in args:
        print(i)


# func(1,2,3,4)
# func(8,9)
# func()

# TODO: variable length keyword arguments
def func2(**kwargs):
    # print("kwargs: ", kwargs)
    # print("type of kwargs: ", type(kwargs))

    for k,v in kwargs.items():
        print(f"key is : {k} and val is : {v}")

# func2(fName = "John", lName = "Doe")

def func3(n1, n2, *args, **kwargs):
    print(f"n1 is: {n1} and n2 is: {n2}" )
    print(f"args is: {args}")
    print(f"kwargs is: {kwargs}")

# func3(4,5,6,7,8,name="John doe")


# TODO: lamda functions
# anonymous functions
'''
there is no return keyword

variable_name = lambda parameters : return expression

'''

cube = lambda x : x ** 3

# print(cube(2))

add = lambda n1, n2 : n1+n2
# print(add(3,4))

# TODO: if and else in the lambda
# lambda: arguments: <if statement> if <condition> else <else statement>

res = lambda num : "It is divisible by 5" if num%5 == 0 else "Not divisible by 5"

# print(res(25))
# print(res(2))

# TODO: usage of lambda functions
# TODO: map -> To get a new list of elements from the existing list on the basis of the logic

# nums = [1,2,3,4,5]
# squares = list(map(lambda num: num ** 2, nums))
# print(squares)

# TODO: filter -> It will filter out the values from the data
# nums = [1,2,3,4,5,6,7,8,9]
# even = tuple(filter(lambda num: num%2==0 , nums))
# print(even)

# TODO: reduce
from functools import reduce
nums = [1,2,3,4,5,6,7,8,9]
sum_of_nums = reduce(lambda n1,n2: n1 + n2, nums)
# print(sum_of_nums)

# TODO: even nums
def isEven(num):
    return num%2 == 0

if isEven(5):
    print("Yes it is even num")
else:
    print("It is odd num")