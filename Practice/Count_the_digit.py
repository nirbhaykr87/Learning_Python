import math
num = int(input("Enter you number"))

"""Brute force:
divide the number by 10 and count how many times it got divided"""


# Optimal solution 
if num==0:
    cnt=1
else:
    # cnt = int(math.log10(num)+1) 
    # what if number is negative so we have to make it as abs number 
    cnt = int(math.log10(abs(num))+1) 


print(f"The total digits in number is {cnt} ")