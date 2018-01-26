#print an element in a dictionary
dic = {"Name": "Sadat Kollan", "Age": 90, "Class":"First Class"}
dic2 = {"Name": "Ramzy Bolten", "Age": 27, "Class":"Lord of Winterfell", "Status":"Dead"}
print dic['Name']

#change value in key in dictionary
dic['Name'] = "harvard"
print dic

# delete a key and value from a dictionary
del dic['Name']
print dic

# remove every element from a dictionary
dic.clear()
print dic

# totally remove a dictionary
del dic
print dic
 
# compare dictionaries
compare = cmp(dic, dic2)
print compare

# length
print len(dic2)

# print dictionary as a string
print str(dic2)

# see type
print type(dic)

# clear a dictionary
print dic.clear()

# copy a dictionary
dic3 = dic2.copy()
print dic3

# print the key-value pairs
print dic2.items()

# print dictionary keys
print dic.keys()

# print dictionary values
print dic.values()
