# enter number: 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4

tr = int(input("enter number: "))
for i in range(1, tr+1):
    for j in range(1, i+1): # i =4
        print(j, end=" ")
    print()


