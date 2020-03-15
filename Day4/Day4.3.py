# 1. Print using while loop number from 5 to 1
# 2 Print using while loop from 10 to 1 and skip 5.

i = 11
while i > 1:
    i -= 1
    if i == 5:
        continue
    print(i)

