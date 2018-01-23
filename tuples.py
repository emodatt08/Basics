tuples are different form list because they cannot be changed, they are represented with paranthesis

tup1 = ('mathematics', 'physics', 'accounting')
print(tup1)

tup2 = ('1', '2', '3')
print(tup2)

tup3 = (1, 2.98, 'uiloo')
print(tup3)

tup4 = (4,)
print(tup4)

tup5 = ('Renji Abarai','Ichigo Kurasaki')
tup6 = (18.000, 400)
tup7 = tup5 + tup6
print tup7

#delete a tuple
del tup1
print tup1

#length of a tuple
print len(tup1)

tupString = ('Hi')
print(4 * tupString)

tupInt = (1,2,3,4,5,6)
print 5 in tupInt

#for loop through a tuple
for i in tupInt:
    print i

#indexing a tuple
L = ('spam', 'Logger', 'Mails')
print L[-2]

#slicing
print L[:1]

#compare two tuples
tup1 = (1,2,3,4,5,6)
tup2 = (4,6,7,2,1,8)
print cmp(tup1, tup1)

#maximmum value
print max(tup1)

#minimum value
print min(tup2)

#convert list to tuple
lists = [1,2,3,4,5]
print tuple(lists)