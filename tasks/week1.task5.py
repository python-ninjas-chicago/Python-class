# Please enter list A: apple banana cherry mango carrot cabbage potato
firstline = input("Please enter your first line: ")
secondline = input("Please enter your second line: ")

firstline = firstline.split()
secondline = secondline.split()

if secondline[0] in firstline:
    print("{} is in first list".format(secondline[0]))
else:
    print("{} is not in first list".format(secondline[0]))

if secondline[1] in firstline:
    print("{} in first list".format(secondline[1]))
else:
    print("{} is not in first list".format(secondline[1]))

if secondline[2] in firstline:
    print("{} in first list".format(secondline[2]))
else:
    print("{} is not in first list".format(secondline[2]))