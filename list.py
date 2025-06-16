marks=[22,44,33,66,77,99] # list is mutable means we can change index
                           # allowing slicing
print(marks)
print(type(marks))
print(len(marks))

marks[0]= 90

print(marks)

print(marks[0:3])
#append or mutation
mylist = [8,5,7,1,4,3]
mylist.append(6)
print(mylist)
#sort or ascending order
mylist.sort()
print(mylist)
#sort descending order
mylist.sort(reverse=True)
print(mylist)
#reverse or backward
mango = ["d","a","r","t"]
mango.reverse()
print(mango)

#insert or add a new value in between index
mango.insert(2,"b")
print(mango)
#remove type value
mango.remove("b")
print(mango)

#pop type index
mango.pop(1)
print(mango)
# append add values in a list
fruits=[]
mov1 ="mango"
mov2 ="kelaa"
mov3 ="banana"

fruits.append(mov1)
fruits.append(mov2)
fruits.append(mov3)
print(fruits)







