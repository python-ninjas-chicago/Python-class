N = int(input())
for i in range(N):
    A_quantity = int(input())
    A_subset = set(input().split())
    B_quantity = int(input())
    B_subset = set(input().split())
    print(A_subset.issubset(B_subset))