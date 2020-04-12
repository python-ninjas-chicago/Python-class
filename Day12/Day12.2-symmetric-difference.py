N = input()
line1 = set(map(int, input().split()))
M = input()
line2 = set(map(int, input().split()))
unionset = line1.union(line2)
interset = line1.intersection(line2)
result = unionset.difference(interset)
for i in sorted(result):
    print(i)
