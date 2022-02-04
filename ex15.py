#reverse word
str ="learning python is easy"


#split this to several parts based on space
words = str.split()
print(words)

#now it wil be in a list, from end we need to print
words= words[-1::-1]
#two -1 to come from back and skip one
print(words)

#this is like list, we need it as a string
#so have a 
outputstr = ' '.join(words)
print(outputstr)
