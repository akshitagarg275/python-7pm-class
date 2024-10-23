'''
Constructor -> It is a method that gets executed as soon as the object of the class is created
def __init__(self)
'''


class Human:

    # def __init__(self):
    #     print("Constructor is called")

    def __init__(self, name, a):
        self.name = name
        self.age = a

    def profile(self):
        return f"Name is : {self.name} and age is : {self.age}"

obj = Human("John", 23)
print(obj.profile())

obj2 = Human("JAck", 25)
print(obj2.profile())