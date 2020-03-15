myList = ["spam", "egg", "salad"]

myList.append("cola")
print(myList)
myList.insert(0, "bread")
print(myList)
myList.remove("salad")
print(myList)
myList.pop(0)
print(myList)
del myList[0]
print(myList)
myList.clear()
print(myList)

print("=========================")
hisList = ["table", "chair", "people", "desk"]
myList = [7, 5]
#myList = hisList
#myList = hisList.copy()
#print(myList)
#myList = myList + hisList
#print(myList)

myList.extend(hisList)
print(myList)