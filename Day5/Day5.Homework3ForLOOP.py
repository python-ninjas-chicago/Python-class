#3)	Write script which counts all “a” and “e” letters from the string you type.
#•	Ex:
#•	Enter sentence: I like reading books and scientific managines.
#•	Output > a  appears 4 times
#•	Output > e appears 4 times

anystring = input("Enter sentence:")
acount = 0
ecount = 0
for imcrazy in anystring:
    if imcrazy == "a":
       acount += 1
    if imcrazy == "e":
        ecount += 1
print("a appears {} times".format(acount))
print("e appears {} times".format(ecount))

