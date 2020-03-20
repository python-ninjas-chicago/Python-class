letters = ("I like reading books and magazines")
count = 0
count1 = 0
for letter in letters:
    if letter == "a":
        count = count + 1
    if letter == "e":
        count1 = count1 + 1
print(f"A letter in this sentence are {count}.")
print(f"E letter in this sentence are {count1}.")
