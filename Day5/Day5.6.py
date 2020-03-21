# add items to the cart using function.
# any value should be entered from cmd
# With loop add items from anystring to mybucketlist using function to add to list.

def addtobucket(anylist, i):
    i = i + " juice"
    anylist.append(item)


mybucketlist = []
while True:
    item = input("Enter item:")
    if item != "quit":
        addtobucket(mybucketlist, item)
    else:
        break

print(mybucketlist)
