'''
property decorator -> it makes the method to be used like an attribute
'''

class Student:
    def __init__(self, name, id):
        self.name = name
        self.__id = id  #private attribute

    @property
    def id(self):
        return f"{self.__id}"
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id

obj = Student("Lokesh", 12)
obj.id = 15
print(obj.id)
