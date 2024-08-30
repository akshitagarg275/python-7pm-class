'''
In python, loops also have the else block
This else block gets executed only the while loop is completely executed
There is no external abruption in the loop execution
'''

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Loop has been executed completely")

for i in range(5):
    if i == 3:
        continue
    print(i)
else:
    print("Loop has been executed completely")