# TODO: conditionals

'''
we want to execute certain code only if the condition is true
only if
if else
if elif
'''

# TODO: only if
'''
if <condition> :
    //if statements
'''

# age = 1

# if age >= 18:
#     print("You can drive the car!")
#     print("I am inside if statment")


# TODO: if else pair
'''
if <condition> :
    //if statements
else:
    //else statements
'''

# age = 2

# if age >= 18:
#     print("You can drive the car!")
#     print("I am inside if statment")
# else:
#     print("You cannot drive the car!")

# TODO: WAP to check if the given no is positive, negative or zero

# num = 0

# if num > 0 : 
#     print(f"{num} is positive")
# elif num < 0 :
#     print(f"{num} is negative")
# elif num == 0:
#     print(f"number is zero")
# else:
#     print("Enter a valid number")


# print("Outside of the if block")
# print("More lines of code")


# TODO: grading system
marks = 78

if marks >= 90 and marks <= 100:
    print("GRADE A+")
elif marks >= 80:
    print("GRADE: A")
elif marks >= 70:
    print("GRADE B+")
elif marks >= 60:
    print("GRADE B")
elif marks >= 50:
    print("GRADE C+")
elif marks >= 40:
    print("GRADE C")
else:
    print("GRADE F")

# TODO: feedback system
'''
take the rating b/w 1-5
'''

# TODO: Nested if else
# WAP to find largest among 3 nos
# num1 = 15
# num2 = 100
# num3 = 12

# if num1 >= num2:
#     if num1 >= num3:
#         print(f"{num1} is greatest")
#         # print(num1, " is greatest")
#     else:
#         print(f"{num3} is greatest")
# else:
#     if num2 >= num3:
#         print(f"{num2} is greatest")
#     else:
#         print(f"{num3} is greatest")    


# TODO: login 
'''
email, google, facebook
'''
isEmail = True
isGoogle = False
isFacebbok = False

# if isEmail:
#     print("Signed in via email")
# elif isGoogle:
#     print("Signed in via google")
# elif isFacebbok:
#     print("Signed in via facebook")

# if isEmail or isGoogle or isFacebbok:
#     print("You are signed in")
# else:
#     print("Please sign in")


# TODO: shopping
isSignedIn = True
isCart = True
isPay = True

# if isSignedIn and isPay and isCart:
#     print("You can purchase the product")
# else:
#     print("Purchase not processed")

if isSignedIn:
    if isCart:
        if isPay:
            print("You can make the purchase!")
        else:
            print("Payment method is not correct")
    else:
        print("Cart is empty")
else:
    print("Not signed in")