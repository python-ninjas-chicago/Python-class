A = set(input().split())
n = int(input())
for i in range(n):
    otherset = set(input().split())
    result = A.issuperset(otherset)
    if result is False:
        break
print(result)
