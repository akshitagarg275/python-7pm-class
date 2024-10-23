# Static Method
'''
We create the static methods when we do not need the method execution to be dependent on the object
'''

class Employee:

    @staticmethod
    def greet():
        print("Good Mornning!")

obj = Employee()
obj2 = Employee()

obj.greet()
obj2.greet()