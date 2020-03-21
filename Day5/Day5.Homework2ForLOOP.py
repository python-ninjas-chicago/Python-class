#2)	Using while loop add all entries to the list, until you type exit. Print list.
#•	Ex:
#•	add item: apple
#•	add item: banana
#•	add item: mango
#•	add item: watermelon
#•	add item: orange
#•	add item: exit
#•	Output > [“apple”, “banana”, “mango”, “watermelon”, “orange”]

bucket = []
while 1 == 1:
    item = input("Enter item: ")
    if item == "quit":
        break
    bucket.append(item)
 
print(bucket)
