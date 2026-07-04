
def decorators(funct):
    def modify(*args , **kwargs):
        print("We are calculating the sum ")
        x = funct(*args , **kwargs)
        print(x)
        print("Thanks for using this function")
        return 

    return modify




@decorators
def add (*args , **kwargs):
    return f"The total sum is {sum(args)}"

print(add(2,4))