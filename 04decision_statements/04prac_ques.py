# TODO: WAP to count the digits in a given num
'''
3465 -> 4
786 -> 3
12 -> 2
'''

num = 786
# num = 12
count = 0
sum_of_digits = 0
mul_of_digits = 1
while num > 0:
    rem = num % 10
    sum_of_digits = sum_of_digits + rem
    mul_of_digits = mul_of_digits * rem
    count = count + 1
    # re-initialization
    num = num // 10

# print("No of digits: ", count)
# print("Sum of digits : ", sum_of_digits)
# print("Mul of digits: ", mul_of_digits)


# TODO: WAP to reverse a given no

# 786 -> 687

num = 786
rev_num = 0
while num > 0 :
    rem = num % 10
    rev_num = (rev_num * 10) + rem
    print("Rev Num: ", rev_num)

    num = num // 10

print("Reverse num is: ", rev_num)
