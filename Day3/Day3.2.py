a = 22
b = 200
if b < a:
    print("b is greater than a")
    print("test")
    print("test")

print("out of if")
#out of if

print("=================")

a = 300
b = 300
if a > b:
    print("a is bigger than b")
elif b > a:
    print("b is bigger than a")
else:
    print("a is equal to b")
# a is equal to b

print("=================")

a = 200
b = 250
print("A is bigger") if a > b else print("B is bigger")
#B is bigger

print("=================")

a = 4
b = 6
c = 4
if a > b or a > c:
    print("a is not smallest")
else:
    print("a is smallest")
#a is not smallest

print("++++++++++++++++")

a = 25

if a > 20:
    print("a is bigger than 20")
    if a > 30:
        print("a is bigger than 30")
    else:
        print("a is smaller 30")

#a is bigger than 20
#a is smaller 30
print("Pass example is here:")
a = 20
b = 30
if b > a:
    pass # Just don't do anything in that if else condition
else:
    print("Test")





