
""" 
 1. by using default arguments
class Calculate:
    def add(self , a , b , c=None):
        if c is None:
            return f"sum is {a+b}"
        
        else:
            return f"Sum is {a+b+c}"


    

cal1 = Calculate()
print(cal1.add(1 , 2)) # ouput - 3
print(cal1.add(1 , 2 , 5)) # ouput - 8

"""

# ---------------------------------------------------------
'''
 2. by using variable length
class Calculate:
    def add(self , *args):
        return f"The sum is {sum(args)}"
        


    

cal1 = Calculate()
print(cal1.add(1 , 2)) # ouput - 3
print(cal1.add(1 , 2 , 5)) # ouput - 8

'''

class Info:
    def stInfo(self , **kwargs):
        return type(kwargs)
    

st1=Info()
print(st1.stInfo(name="Nirbhay", course="Btech"))