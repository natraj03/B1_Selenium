
mylist = [2,3,4,"u",5,"k","d"]
output = 0


for index in range(0,len(mylist)):
     tempVar = mylist[index]
     if type(tempVar) == str:
         print("string",tempVar)
