#OOPS Concepts
'''
Object Oriented Programming System
class -> It is a blueprint (It is in the theory)
object -> It is real world entity 

A class consist of 
- attributes (variables)
- methods (functions)

4 pillars of OOPS
- abstraction : Hiding the details
- encapsulation : combining the attributes and methods together under one entity
- inheritance : super(parent) class ---> derive(child) class 
- polymorphism : poly(many) + morph(forms)
'''

class Human:
    # class attributes: When any object will be created, it will have same value
    eyes = 2
    nose = 1

    def greet(self):
        print("Hey, Human!")

# creating object
obj = Human()
obj1 = Human()
# print(obj)
# print(type(obj))

# print(obj.eyes)
# obj.greet()
# Human.greet(obj)


print(obj.eyes)
# obj.eyes = 3
Human.eyes = 5
print("AFTER: ")
print("obj.eyes: ", obj.eyes)
print("obj1.eyes: ", obj1.eyes)