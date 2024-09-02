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

profile3(age=24, name="John")

# TODO: varibale length arguments
# TODO: variable length keyword arguments
# TODO: lamda functions
