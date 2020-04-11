if __name__ == '__main__':
    s = input()
    alnum = False
    alph = False
    digit = False
    lowcase = False
    uppercase = False
    for char in s:
        if char.isalnum():
            alnum = True
        if char.isalpha():
            alph = True
        if char.isdigit():
            digit = True
        if char.islower():
            lowcase = True
        if char.isupper():
            uppercase = True

print(f'{alnum}\n{alph}\n{digit}\n{lowcase}\n{uppercase}')
