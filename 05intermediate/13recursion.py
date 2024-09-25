# RECURSION
'''
A method calling itself is recursion

bigger problem --> divide the problem into smaller parts --> find the solution for smaller problem



'''

# TODO: find the factorial
'''
5! = 5*4*3*2*1 = 120

5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1

factorial(num) = num * factorial(num - 1)

Base case:
if num == 1:
    return 1
'''

def fact(num):
    # base case
    if num == 1:
        return 1
    
    return num * fact(num - 1)


# print(fact(3))


# TODO: fibonacci series num
# 0 1 1 2 3 5 8 13

'''
fib(num) = fib(num -1 ) + fib (num - 2)

base case:
if num == 1 or num == 0:
    return num
'''

def fact(num):
    # base case
    if num == 1 or num == 0:
        return num
    return fact(num - 1) + fact(num - 2)

print(fact(3))