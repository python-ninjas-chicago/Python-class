# Guess the word
# Create a list 20 fruits and vegg: apple banana carrot pear avocado mango .......
# randomly select any fruit from list and let the person to guess it by entering letters:

#enter whole word or letter: t
#Sorry letter not in the word
#enter whole word or letter: p
#Letter p exists in the word
#enter whole word or letter: r
#Letter r exists in the word
#enter whole word or letter: pear
#Yahoo, you got it! It's pear!

import random
random_list = ["apple", "peach", "mango", "banana", "grapes", "strawberry", "raspberry", "orange", "pear", "tomato",
               "carrot", "onion", "potato", "cucumber", "pumpkin", "cabbage", "garlic", "watermelon", "apricot",
               "avocado"]
secret_word = random.choice(random_list)
count = 0
right_guessed = []
while True:
    guess = input("Please enter word or a single letter:")
    count += 1
    if guess == secret_word:
        print(f"Hey you did good job, {secret_word} is right word.")
        break
    elif guess in secret_word:
        right_guessed.append(guess)
        print(f"{guess} is in the word!")
    else:
        print("Try another letter or word")
    print(f"Letters in words:{right_guessed}, number of guesses: {count}")















