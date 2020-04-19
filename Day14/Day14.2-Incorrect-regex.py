import re
N = int(input())
for _ in range(N):
    line = input()
    try:
        print(bool(re.compile(line)))
    except:
        print(False)