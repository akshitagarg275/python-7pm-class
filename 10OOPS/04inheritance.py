'''
Inheritance -> Child class derives from the parent class
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
'''

# TODO: Single Inheritance

class Human:
    def __init__(self):
        print("Class Human")

    def breathe(self):
        print("Humans can breathe")


class Employee(Human):
    org = "ABC"

    def __init__(self):
        print("I am employee class")

    def breathe(self):
        print("Yeah, breathing !!")
        super().breathe()

e1 = Employee()
e1.breathe()