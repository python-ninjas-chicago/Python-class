a = 40
b = 50
c = 30
if a > b:
    print("{} is greater than {}".format(a, b))
elif a == b:
    print("{} and {} are equal".format(a, b))
else:
    print("{} is greater than {}".format(b, a))


if a > b or a > c:
    print("a is not smallest")
else:
    print("a is smallest")
print("============================")

