#if statement
a = 5
if(a == 5):
    print "A is equal to 5"
else:
    print "A is not equal to 5"    


#if / elif
a = 6 * 7

if( a > 36 ):
    print "A is greater than 36 and its equal to " + str(a) 
elif(a < 36):
    print "A is less than 36 and its equal to " + str(a)
else:
    print "A is just equal to " + str(a)     


# Nested ifs
a = 15
b = 89
c = 34

if( a == 16):
    if(b == 89):
        print "A is equal to " + str(a) + " and B is equal to " + str(b) 
else:
    if(c == 34):
        if(a == 15):
            print "C is equal to " + str(c) + " and A is equal to " + str(a)
        else:
            print "C is not equal to 15"            