
try:
    print(y)
except:
   print("There is an error, fix it")

print("===================================")
y = "test"
x = 6
try:
    print(y + x)
except NameError:
    print("where y is not defined")
except TypeError:
    print("you have type error")
except:
    print("There is something wrong, I don't know")

try:
    print(y + x)
except:
    print(f'{y} + {x}')

print("===============================")
print("===============================")

try:
    f = open("file.txt")
    f.write("Hello")
except:
    print("Something wrong with file.")
finally:
    f.close()
print("===============================")

x = 1
if x < 0:
    raise Exception("Hey, x can not be below zero")

print("=================================")

z = "This is test string"
#z = 1
if not type(z) is int:
    raise TypeError("z should be integer")