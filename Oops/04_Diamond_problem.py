class A:
    def show(self):
        return "A"

    
class B(A):
    def show(self):
        return "B"
    
class C(A):
    def show(self):
        return "C"
    
class D(B , C):
    pass
    # def show(self):
    #     return "D"

obj1 = D()
print(D.mro())  # This will show the Method Resolution order that follow to print show function
print(obj1.show())
    

    
