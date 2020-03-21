#enter number: 10
#a   b
#1 * 1 = 1
#1 * 2 = 2
#1 * 3 = 3
#.....
#
#2 * 1 = 2
#2 * 2 = 4
#....
#
#5 * 1 = 5
#...
#9 * 9 = 81
#9 * 10 = 90
# ....
#10 * 1 = 10
#....
#10 * 10 = 100

for a in range(1, 11):
    for b in range(1, 11):
        print("{} * {} = {}".format(a, b, a * b))
        # print(f"{a} * {b} = {a * b}")
        # print(str(a) + " * " + str(b) + " = " + str(a * b))
    print()
















