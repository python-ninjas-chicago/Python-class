N = int(input())
mydictionary = {}
for i in range(N):
    name = input()
    score = float(input())
    mydictionary[name] = score
minimum = sorted(mydictionary.values())[0]
second_minimum = 1000
for i in sorted(mydictionary.values()):
    if minimum < i:
        second_minimum = i
        break
for j in sorted(mydictionary):
    if second_minimum == mydictionary.get(j):
        print(j)

