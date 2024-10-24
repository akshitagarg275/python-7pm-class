'''
2d -> 3i^ + 4j^
3d -> 4i^ + 5j^ + 9k^
'''

class Vec2d:

    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    
    def printVec(self):
        return f"{self.icap}i^ + {self.jcap}j^"
    
class Vec3d(Vec2d):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def printVec(self):
         return f"{self.icap}i^ + {self.jcap}j^ + {self.kcap}k^"

obj = Vec2d(4,5)
print(obj.printVec())

obj2 = Vec3d(2,3,5)
print(obj2.printVec())