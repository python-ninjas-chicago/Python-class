#1)	Using range(1, 50), make two list, one containing all even numbers
# and other containing all odd numbers.
#Ex: Output example [1, 3, 5, ……..], [2, 4, 6, ……]

evennumbers = []
oddnumbers = []

for i in range(1, 51):
    if i % 2 == 0:
        evennumbers.append(i)
    else:
        oddnumbers.append(i)
print("Even numbers: {}".format(evennumbers))
print("Odd numbers: {}".format(oddnumbers))