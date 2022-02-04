#14
#takes a list and returns new list containing all elements of first list
#minus duplicates

#using loop 

def duplicateremovedlist(x):
    newlist = [1,2,3,5]
    for i in x:
        if i not in newlist:
            newlist.append(i)
    return newlist


a= [1,2,4,5,7,1,9]
print(a)
#printing duplicate removed whole list
print (duplicateremovedlist(a))


