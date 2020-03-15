for i in range(5):
    print(i)
#0
#1
#2
#3
#4
print("======================")

basket = ["apple", "cherry", "banana", "carrot"]
for j in basket:
    print(j)
#apple
#cherry
#banana
#carrot
print("============================")

for x in "banana":
    print(x)
# b
# a
# n
# a
# n
# a

print("==================================")

cart = ["apple", "cherry", "banana", "carrot"]

for x in cart:
    print(x)
    if x == "cherry":
        break
#apple
#cherry

print("======================================")

for x in cart:
    if x == "cherry":
        break
    print(x)
# apple

print("=====================================")

basket = ["apple", "cherry", "banana", "carrot"]

for fruit in basket:
    if fruit == "cherry":
        continue
    print(fruit)
# apple
# banana
# carrot
print("=======================================")

for x in range(5, 11):
    print(x)
print("=========================================")
for x in range(5, 10, 2):
    print(x)
print("====================================")

fruits = ["apple", "mango", "pear", "pineapple"]
mix = ["juice", "shake"]
for i in fruits:
    for j in mix: #  i pineapple - j juice, j shake
        print(i, j)
print("==========================================")
for i in range(3):
    for j in range(3):
        print(i, j)



