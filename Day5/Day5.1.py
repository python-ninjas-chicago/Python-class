# Enter the number: 5
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1
#

tr = int(input("enter number: "))
for i in range(tr+1, 1, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()