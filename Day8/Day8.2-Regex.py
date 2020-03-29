import re

text = "We are trying to learn python!"

x = re.search("^We.*python!$", text)

if x:
    print("Yes, I see match!")
    print(x)
else:
    print("There is no match!")

print("=========================")

x = re.findall("^We.*python!$", text)

if x:
    print(x)
else:
    print("There is no match!")

print("==========================")

#[a-z]*  in a-z 0 or more occurences
#[a-z]+  in a-z 1 or more occurences
# \d and [0-9]  any digit number
# ^ starts with
# $ ends with
# . any character
# a|b   or a or b
# \w any character from a-Z or 0-9 _
# \s whitespace
# \b begins

text1 = "Today is good day for walking outside."
y = re.split("\s", text1)
print(y)

print("=========================================")

txt2 = "I have have a cool dell delete monitor!"
z = re.sub("d[a-z]+l\s", "samsung ", txt2)
print(z)
print("==============================================")

txt3 = "I hope rain will stop today! and tomorrow!"
h = re.search(r"\bt\w+!", txt3)
print(h.string)
print(h)

txt3 = "I hope rain will stop today! and tomorrow!"
t = re.findall(r"\bt\w+!", txt3)
print(t[0], t[1])

