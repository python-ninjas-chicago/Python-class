def swap_case(s):
#without swapcase
    a = ''
    for i in s:
        if i.islower():
            a+=i.upper()
        elif i.isupper():
            a+=i.lower()
        else:
            a+=i
    return a
#with swapcase
#   return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)