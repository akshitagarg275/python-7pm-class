# TODO: generators
'''
yield keyword is used instead of return
'''

def my_gen():
    yield 1
    yield 2
    yield 3

# for val in my_gen():
#     print(val)

# x = my_gen()
# # print(x)
# print(next(x))
# print(next(x))


# TODO: Create two generators for fibonacci numbers
def fib(limit):
    a,b = 0,1
    yield a
    while b < limit:
        yield b
        a, b = b, a+b

# x = fib(200)

# for i in x:
#     print(i)

# def state_gen():
#     value = yield
#     while True:
#         value = yield value * 2

# gen = state_gen()
# next(gen)
# print(gen.send(10))

# TODO: exception handling in generator
def error_handling_generator():
    try:
        yield 1
        yield 2
        raise ValueError("An error occurred")
        yield 3
    except ValueError as e:
        print(e)

# gen = error_handling_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))  # This will trigger the exception


# TODO: Handling exception handling outside the generator
def gen_with_error():
    yield 1
    raise ValueError("Error inside generator")

g = gen_with_error()
print(next(g))
try:
    g.throw(ValueError, "Error thrown")
except ValueError as e:
    print(e)