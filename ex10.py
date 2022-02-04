#10

list1 = [ 11,12,13,14,15,16]
list2 = [ 21,12,13,14,25,26,15]
result1 = [i for i in list1 if i in list2]
print(result1)



#list comprehension using 2 lists random no's
import random
#we are going to generate random nos in 2 lists

list1 = random.sample(range(1,15),13)
list2 = random.sample(range(1,15),14)

result2 = [i for i in list1 if i in list2]
print(result2)
