l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
l3.append(42)
x = len(l3)
print(13, x)

class vector:
    def initialize(self, x, y): #меетод
        self.x = x
        self.y = y 
    
    def dln(self):    #меетод
        return (self.x ** 2 + self.y ** 2)** 0.5
        
v4 = vector()
v4.initialize(4, 8)
print(v4.dln())

l = [1, 2, 3, 9, 8, 7]

ll = []
for t in ll:
    ll.append(t**2)
    
ll = [t**2 for t in l]




"""
v1 = vector()
v1.x = 1
v1.y = 2

def dln(v):
    return (v.x ** 2 + v.y ** 2)** 0.5
a = dln(v1)

v2 = vector()
v1.X = 1
v1.Y = 2

#a_1 = dln(v2)

def initialize(v, x, y):
    v.x = x
    v.y = y 
v3 = vector()
initialize(v3, 5, 7)
print(dln(v3))
"""
l = [10,21, 34, 47, 59, 60]
