#!/bin/python3
# Complete the solve function below.
def solve(s):
    result = ''
    for i in range(len(s)):
        if s[i-1] == " " or i == 0:
            result+=s[i].upper()
        else:
            result+=s[i]
    return result

print(solve(input()))



