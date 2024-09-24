# TODO: Exception Handling
'''

Types of errors:
- syntax error
- Logical error ->
    2 + 2 = 4
    '2' + '2' = 22
- run time error
    someone has given wrong input
    file is not present
    wrong url is accessed

Exception handling helps us to handle the potentially occurring
errors gracefully

try: 
    //try statements
except:
    //handles the exception
else:
    //else statements
    // either else statements execute or the except statement
finally:
    //finally block statements
    // no matter what finally block gets executed
'''


# num1 = 5
# num2 = 0
# try:
#     print(num1/num2)

# except ZeroDivisionError as e:
#     print(e)
#     print("Denominator cannot be")

# except BaseException as e:
#     print("Error: ", e)
#     print("There is an exception")

# print("Some other lines of code....")

# a = 4
# try:
#     print(a)
# except BaseException as e:
#     print("Error: ", e)
# else:
#     print("This is else part")
# finally:
#     print("This is the finally block part")


def func():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4

# print(func())

# TODO: raising an exception

# name = "John"

# if name == "John":
#     raise "John is not allowed"
