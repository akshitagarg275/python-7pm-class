# Operators -> To perform certain operations
'''
unary operators -> only one operand is required
binary operators -> in which two operands are required

artithmetic operator
assignment
relational
logical
bitwise
membership
'''

# TODO:  unary operator
# a = -3
# print(a)

# TODO: artithmetic 
num1 = 5
num2 = 2
# print("add is : ", num1 + num2)
# print("sub is : ", num1 - num2)
# print("mul is : ", num1 * num2)
# print("div is : ", num1 / num2)

# % modulus operator ->  provides the remainder
# print("remainder is : ", num1 % num2)

# floor division (//) -> it provides integer quotient
# print("int quotient is : ", num1 // num2)

# exponentational operator (**)
# print("5 raise to power 2 is: ", 5**2)


# TODO: assignment operator (=)
# assigning the right hand side object to a reference variable
# a = 2
# print(a)

# x = 5 * 2
# print(x)

# num1 = num2 = num3 = 5

# shorthand notation
# a = a + 3
# a+= 3
# print("after: ",a)

# TODO: relational operators(comparison operators)
'''
These return the boolean values (True/False)
> : greater than
< : lesser than
>= : greater than or equal to 
<= : lesser than or equal to
== : equality
!= : not equal to
'''
# print( 5 > 3)
# print(5 >= 5)
# print(5 >= 7)
# print(6 < 3)
# print(3 == 3)
# print("John" == "John")
# print(2 != 1)

# TODO : logical operators
'''
and : if any one input is False output will be False 
or : if anyone input is True output will be True
not : it simply makes True to False , False to True
'''

# print(5>3 and 3>2)
# print(5<3 and 4>2)

# print(5>3 or 3>2)
# print(5<3 or 4>2)

# Falsy values -> None, 0, False, '', []
# print(not 0)
# print(not [])
# print(not -3)

# TODO: bitwise operators
'''
They directly work on the bits
& -> bitwise and
| -> bitwise or
^ -> bitwise xor
<< -> left shift
>> -> right shift
'''

# print(5 & 8)
# print(5 | 8)

# print(5 ^ 8)

# print(5 << 1)

# print(5 >> 1)


# TODO: membership operator (in)
nums = [1,2,3,4]
# print(1 in nums)
# print(1 not in nums)

name = "John"
# print('n' in name)


# TODO: identity operator(is)
# It checks whether the object variable
# is pointing to same memory location or not
a = 5
# print(id(a))
# print(a)

# b = 5
# print(id(b))

# print(a is b)

# b = 4

# b = a
# print(b)

# b = 3
# print("after b: ", b)
# print("after a: ",a)



# list1 = [1,2,3]

# list2 = list1

# print("before list1: ",list1)
# print("before list2: ",list2)
# print(list1 is list2)

# list2[0] = 99

# print("after list1: ",list1)
# print("after list2: ",list2)


# list3 = [1,2,3]
# list4 = [1,2,3]

# print(list3 == list4)
# print(list3 is list4)

# list4[0] = 99
# list4[1] = 89

# print(list3)
# print(list4)


# name = "John"
# print(id(name))
# name = "Jenny"
# print(id(name))
# print(name)