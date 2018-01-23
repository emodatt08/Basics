
#show raw statement
print(r"doesn't")

#string formatting
string = "One, %s, three" % 'two'
print(string)


#number formatting
number = "1, %d, 3" %2
print(number)

#using multiple lines
print("""
This
is
Pycharm
IDE
""")

#print string multiple times
print(5 * ' hello')

#index string from right side
word = "Hillary"
print(word[-1])

#slice string
name = "Hillary"
new = name[0:4]
print(new)

#split string
sentence = "Hi my name is Hillary Kollan"
words =sentence.split(" ")
print(words)

#uppercase
sentence = "Hi my name is Hillary Kollan"
uppercase =sentence.upper()
print(uppercase)

#lowercase
sentence = "Hi my name is Hillary Kollan"
lowercase = sentence.lower()
print(lowercase)



#capitalize
sentence = "haemoglobin"
uppercase = sentence.capitalize()
print(uppercase)
