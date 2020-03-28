# =================== lambda =======================
x = lambda  a: a + 1
print(x(1))

y = lambda a: a**2
print(y(2))

z = lambda a, b: a * b
print(z(2, 3))

k = lambda a, b, c, d: a + b + c + d
print(k(3, 4, 5, 2))

print("===========================")
def mylambda(k):
    return lambda a: a * k

Ulan = mylambda(9)
print(Ulan(6))
print("============================")

def powerof(k):
    return lambda a: a**k

power_of_2 = powerof(2)
power_of_3 = powerof(3)

print(power_of_2(8))
print(power_of_3(5))

print("===========================")
a = ["a", "b", "c"]
print(a[0])
print("==============================")
print("==============================")

#========== Classes/objects =================
class myclass:
    x = 5

p1 = myclass()
print(p1.x)
print("===============================")

class Person:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

p1 = Person("Almas", 21)
p2 = Person("Vitya", 12)
print(p1, p1.age)
print(p2)
print(p1.age, p1.name)
print(p2.name, p2.age)

print("=============================")


class Student:
    def __init__(self, name, age):  # Default built in function
        self.name =  name # self which is object and has attribute name
        self.age = age # self which is object and has attribute age


    def myfunction(self):  # optional function
        print(f"This person's name is {self.name} and age is {self.age}.")


s1 = Student("Mike", 56)
s1.age = 57  # changing age parameter
#del s1.age
#del s1
s1.myfunction() # call myfunction in class Student
print("============================================")
class test:
    pass

t1 = test()
print(t1)
print("=========================================")





