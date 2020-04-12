N = int(input())
setorig = set(input().split())
number_of_commands = int(input())
for i in range(number_of_commands):
    command = input().split()[0]
    com_set = set(input().split())
    if command == "intersection_update":
        setorig.intersection_update(com_set)
    elif command == "update":
        setorig.update(com_set)
    elif command == "symmetric_difference_update":
        setorig.symmetric_difference_update(com_set)
    elif command == "difference_update":
        setorig.difference_update(com_set)
print(sum(list(map(int, setorig))))
