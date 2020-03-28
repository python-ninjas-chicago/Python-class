def sentencescount(data):
    data = data.replace("!", ".")
    data = data.replace("?", ".")
    data = data.split(". ")
    return len(data)

def characterscount(data1):
    count = 0
    for char in data1:
        if char != " ":
            count+=1
        #if char.isalpha():
            #count +=1
    return count


def wordscount(data2):
    words = data2.split()
    return len(words)


sentence = input("Please enter your sentence: ")
print("sentences: ", sentencescount(sentence))
print("words: ", wordscount(sentence))
print("characters", characterscount(sentence))
repl = input("ENter word to replce: ")
repl1 = input("ENter word replace to: ")
print(sentence.replace(repl, repl1))