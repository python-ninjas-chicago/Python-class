# for loop
# while loop
# Example 1
i = 1
while i < 6:
    print("I crazy")
    i += 1
#I crazy
#I crazy
#I crazy
#I crazy
#I crazy

# Example 2

y = 1
while y < 6:
    print(y)
    if y == 3:
        break
    y += 1
#1
#2
#3
print("+++++++++++++++++++++++++++++++")
 # Example 3

j = 0
while j < 6:
    j += 1
    if j == 3:
        continue
    print(j)
#1
#2
#4
#5
#6
print("================================")
# Example 4:
x = 1
while x < 4:
    print(x)
    x += 1
else:
    print("x is not less than 4 anymore")
#1
#2
#3
#x is not less than 4 anymore



