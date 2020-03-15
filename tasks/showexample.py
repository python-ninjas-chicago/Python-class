item1 = input("Please enter item: ")
item2 = input("Please enter item: ")
item3 = input("Please enter item: ")
item4 = input("Please enter item: ")
item5 = input("Please enter item: ")
shoppinglist = [item1, item2, item3, item4, item5]
print("Your shopping list is : {} ".format(shoppinglist))
removeitem = input("Please remove item to remove: ")
if removeitem in shoppinglist:
    shoppinglist.remove(removeitem)
else:
    print("{} doesn't exists".format(removeitem))

print("Your shopping list is : {}".format(shoppinglist))
