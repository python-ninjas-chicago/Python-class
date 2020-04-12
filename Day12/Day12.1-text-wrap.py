import textwrap

def wrap(string, max_width):
    S = ''
    for i in range(len(string)):
        S+=string[i]
        if (i+1) % max_width == 0:
            S+='\n'
    return S

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#
# import textwrap
#
# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)