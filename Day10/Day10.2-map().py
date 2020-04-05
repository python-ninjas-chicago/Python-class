anylist = ['20', '12', '1', '48', '78', '5']
print(anylist)
print(type(anylist[0]))
print("=======================================")
anylist = list(map(int, anylist))
print(anylist)
print("=======================================")
print("=======================================")


def multiplier(x):
    return x*5


mylist = [20, 12, 1, 48, 78, 5]
mylist = list(map(multiplier, mylist))
print(mylist)
print("==========================================")
print("==========================================")

def multiplier(x):
    return "Hello " + x

mylist = ["Ulan", "Merim", "Dina", "Ainura"]
mylist = list(map(multiplier, mylist))
print(mylist)

