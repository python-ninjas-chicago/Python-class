if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # for loop, if break, reverse(), sorted()
    a = sorted(arr)
    a.reverse()
    max = a[0]
    for i in a:
        if i < max:
            print(i)
            break
