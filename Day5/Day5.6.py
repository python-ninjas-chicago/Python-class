# add items to the cart using function.
# any value should be entered from cmd
# With loop add items from anystring to mybucketlist using function to add to list.


def add_to_bucket(your_list, i):
    i = i + " juice"
    your_list.append(i)


my_bucket_list = []
while True:
    item = input("Enter item:")
    if item != "quit":
        add_to_bucket(my_bucket_list, item)
    else:
        break

print(my_bucket_list)
