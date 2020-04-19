#!/usr/bin/python
# Guess the number 1-50
# 32
# 10?
# no, higher
# 40?
# lower
# 30?
# higher
# 32?
# Yes, you nailed it!
# number guesses?

from random import randint
rand_num = randint(1, 50)
count = 0
while True:
    guess = int(input("Guess the number: "))
    count += 1
    if guess > rand_num:
        print("Go lower!")
    elif guess < rand_num:
        print("Go higher!")
    else:
        print(f"You nailed it! Random number is {rand_num}. \nNumber of guess is {count}")
        break