# Use nested for loop.You have two buckets
# bucket1 = ["apple", "banana", "cherry", "peach", "carrot", "plum", "grape"]
# bucket2 = ["apple", "mango", "carrot", "cabbage", "kiwi", "peach"]
# Please identify same fruits/vegetables and add them to one new list

bucket1 = ["apple", "banana", "cherry", "peach", "carrot", "plum", "grape"]
bucket2 = ["apple", "mango", "carrot", "cabbage", "kiwi", "peach"]
sameitems = []

for itema in bucket1:
    for itemb in bucket2:
        if itema == itemb:
            sameitems.append(itema)
print(sameitems)