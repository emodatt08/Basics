import math
#function to add two integers
def add(a, b):
    return a + b

#function to loop an integer 10 times
def loopit(a):
    for a in range(0,10):
         listBox  = (a)
         print listBox     

#function to square an integer       
def squares(a):
   return a * a

#function to convert to a floating point
def floorInt(a):
    return math.floor(a)

def powerInt(a, b):
    return math.pow(a, b)

print powerInt(2, 2)        