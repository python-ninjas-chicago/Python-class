def get_num_of_letters(text):
    counter = 0
    for i in text:
        if i.isalpha():
            counter += 1
    return counter


def get_num_of_words(text):
    words = len(text.split(" "))  # return len(text.split()) >>Shortcut
    return words  ##Counting Words

def get_num_of_sent(text):
    sent = text.rstrip(".").split(".")
    #print(sent)
    return len(sent)  ###Counting Sentences

while True:
    text = input("Please enter your sentence: ")
    if text == "done":
        break
    print("letters:", get_num_of_letters(text))
    print("*" * 100)
    print("words:", get_num_of_words(text))
    print("*" * 100)
    print("sent:", get_num_of_sent(text))
    print("*" * 100)
    print(text.replace('early', 'lately'))
    print("*" * 200)
