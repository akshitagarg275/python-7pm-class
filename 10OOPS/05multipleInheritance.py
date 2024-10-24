'''
Multiple Inheritance -> When a child class derives from 2 parent classes
'''

class A:

    def __init__(self):
        print("I am in class A")
    
    def greet(self):
        print("Greetings from class A")

class B:

    def __init__(self):
        print("I am in class B")

    def greet(self):
        print("Greetings from class B")

class C(B , A):
    def __init__(self):
        print("I am in class C")
        super().__init__()
    
    def greet(self):
        print("I am in class C")
        super().greet()

    
obj = C()
obj.greet()