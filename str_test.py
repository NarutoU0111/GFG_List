class A:
    def __str__(self):
        return 1
    
class B(A):
    def __init__(self):
        super().__init__()
    
class C(B):
    def __init__(self):
        super().__init__()

obj1=A()
obj2=B()
obj3=C()

print(obj1,obj2,obj3)