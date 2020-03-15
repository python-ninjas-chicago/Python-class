mystring = "I will become best in python#"
# 1.a
mystring = mystring.strip("#")
print(mystring)
# 1.b
mystring = mystring.split()
print(mystring[-1])

# 1.c
print(mystring)
mystring.append("!")
print(mystring)

#1.e
mystring.insert(2, "definitely")
print(mystring)

#1.f
a = ["I", "will", "study", "hard"]
# mystring = mystring + a
mystring.extend(a)
print(mystring)

# Task 2
number = input("Please enter your number: ")
if int(number) % 2 == 0:
    print("{} is even".format(number))
else:
    print(number + " is odd")

# Task 3
# Task 4
number1 = input("Please enter you number: ")
number2 = input("Please enter you number: ")
number3 = input("Please enter you number: ")
number4 = input("Please enter you number: ")
number5 = input("Please enter you number: ")
number6 = input("Please enter you number: ")
number7 = input("Please enter you number: ")
number8 = input("Please enter you number: ")
number9 = input("Please enter you number: ")
number10 = input("Please enter you number: ")
numbers = []
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.append(number5)
numbers.append(number6)
numbers.append(number7)
numbers.append(number8)
numbers.append(number9)
numbers.append(number10)
checknumber = input("Please enter number to check: ")
if checknumber in numbers:
    print("It's here, yahoo!")
else:
    print("Not here")


