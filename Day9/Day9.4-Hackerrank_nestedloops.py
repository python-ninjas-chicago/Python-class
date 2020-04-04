if __name__ == '__main__':
    mylist = []
    firstmin = float(101)
    secondmin = float(101)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < firstmin:
            secondmin = firstmin
            firstmin = score
        if score < secondmin and score > firstmin:
            secondmin = score
        mylist.append([name, score])
    mylist = sorted(mylist)
    for i in mylist:
        if i[1] == secondmin:
            print(i[0])