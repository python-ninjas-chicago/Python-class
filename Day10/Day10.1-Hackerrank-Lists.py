N = int(input())
anylist = list()
for i in range(N):
    line = input()
    command = line.split()
    if command[0] == "insert":
        anylist.insert(int(command[1]), int(command[2]))
    elif command[0] =="print":
        print(anylist)
    elif command[0] == "remove":
        anylist.remove(int(command[1]))
    elif command[0] == "append":
        anylist.append(int(command[1]))
    elif command[0] == "sort":
        anylist.sort()
    elif command[0] == "pop":
        anylist.pop()
    elif command[0] == "reverse":
        anylist.reverse()









