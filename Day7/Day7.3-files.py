#================ FILES =================

# file example

f = open("myinputfile.txt", "r")
print(f.read())
f.close()
print("===================")
d = open("myinputfile.txt", "r")
print(d.readline())
print(d.readline())
d.close()
print("===================")

s = open("myinputfile.txt", "r")
for i in s:
    print(i, end="")
print()
print("========================")

r = open("myinputfile.txt", "a")
r.write("\nThis is another row!")
r.close()
f = open("myinputfile.txt", "r")
print(f.read())
f.close()

print("===========================")
x = open("testfile.txt", "w")
x.write("Oops!")
x.close()
x= open("testfile.txt", "r")
print(x.read())
x.close()

print("=====================")
g = open("filemile.txt", "a")
g.write("Oops!")
g.close()
g = open("filemile.txt", "r")
print(g.read())
g.close()

import os
os.remove("filemile.txt")
os.remove("testfile.txt")




