# add items to the cart using function.
# anystring = "apple cherry berry banana melon"
#With loop add items from anystring to mybucketlist using function to add to list.

def addtobucket(anylist, item):
    anylist.append(item)

mybucketlist = []
anystring = "apple cherry berry banana melon"
anystring = anystring.split()
for i in anystring:
    addtobucket(mybucketlist, i)

print(mybucketlist)
