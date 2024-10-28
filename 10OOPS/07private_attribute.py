'''
creating a private attribute by prefixing double underscore
'''
class Student:
    def __init__(self, name, id):
        self.name = name
        self.__id = id  #private attribute
    
    def getId(self):
        return f"{self.__id}"

obj = Student("Lokesh", 12)
# print(obj.__id)
print(obj.getId())