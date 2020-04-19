N = int(input())
stamps = set()
while N > 0:
    stamps.add(input())
    N-=1
print(len(stamps))