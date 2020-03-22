# Function with multiple elements, *args
def test_function(*students):
    print(students)
    print(students[0])
    lists_students = list(students)
    lists_students[0] = "Merim"
    print(lists_students)


test_function("Mary", "Mike", "Jackie")

#================================
print("===========================")


def function1(student1, student2, student3, student4):
    print(student1)
    print(student2)
    print(student3)
    print(student4)


function1("Katya", "Marina", "Olya", "Irinia")

print("++++++++++++++++++++++++++++++++++++++++++++")


def coolfunction(**students):
    print("Her/His lastname is " + students["lastname"])
    print(students)


coolfunction(firstname="Jackie", lastname="Chan")

print("+++++++++++++++++++++++++++++++++++++++++++++++")

def my_function(name, city = "USA"):
    print(f"{name} is from {city}")

my_function("Bruce", "New York")
my_function("Jennifer", "Los Angeles")
my_function("Tom")


print("===================================================")


def ulans_function(garage):
    for car in garage:
        print(car)


his_cars = ["camry", "mazda", "honda", "shoha"]
ulans_function(his_cars)
print("=================================================")


def square(x):
    return x * x


print(square(6))
print(square(5))
print(square(8))


print("=======================================================")

#6 + 5 + 4 + 3 + 2 + 1


def myprostofunction(n):                     # n=6
    if n > 0:
        result = n + myprostofunction(n - 1)
        print(result)
    else:
        result = 0
    return result

myprostofunction(a)













