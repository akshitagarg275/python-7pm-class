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
    
class Programmer(Employee):
    language = "python"

    def __init__(self):
        print("Init of programmer class")
        super().__init__()
    
    def breathe(self):
        print("Programmer getting hardly anytime to breathe")
        return super().breathe()

obj = Programmer()
obj.breathe()