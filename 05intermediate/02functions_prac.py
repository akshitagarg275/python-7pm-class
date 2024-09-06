# TODO:  Write a function to calculate and return the square of a number.

def square(num):
    return num ** 2

# print(square(4))

# TODO: Create a function that takes two numbers as parameters and returns their multiplication.

def multiply(n1, n2):
    return n1 * n2

# print(multiply(3,4))

# TODO: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def poly(n1, n2):
    if type(n2) == str:
        int_n2 = int(n2)
        return n1 * int_n2
    return n1 * n2

# print(poly(3,5))
# print(poly("Hello", 2))
# print(poly("Hello", "2"))


# TODO: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "user"):
    print(f"Hello, {name}")

# greet("Sam")
# greet()

# TODO: Create a lambda function to compute the raise to power 5 of a number.

powerOf5 = lambda num : num ** 5
# print(powerOf5(2))

# TODO: Write a function that takes variable number of arguments and returns their sum

def calc_sum(*args):
    sum = 0
    for num in args:
        sum += num
    
    return sum

# print(calc_sum(1,2,3,4))
# print(calc_sum(5,6,7,8))

# TODO: Create a function that accepts any number of keyword arguments and prints them in the format key: value

def key_val(**kwargs):
    for k, v  in kwargs.items():
        print(f"{k} : {v}")

key_val(name="John Doe", course = "python")

