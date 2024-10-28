'''
dunder methods or magic methods
'''

# print(dir(int))

class Num:
    def __init__(self, num):
        self.n = num
    
    def __str__(self):
        return f"object of class Num"
    
    def __add__(self, other):
        return self.n + other.n
    
    def __lt__(self, other):
        return self.n < other.n

n1 = Num(5)
# print(n1)
n2 = Num(6)

# print(n1 + n2)
print(n1 < n2)