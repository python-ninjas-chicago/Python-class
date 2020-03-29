class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def display_salary(self):
        return f"{self.name}'s salary is {self.salary}"

    def calculate_age_(self, in_years):
        return f'{self.name} will be in {in_years} years {in_years+self.age}'


e1 = Employee('Max', 50000, 30)
e2 = Employee('Mike', 90000, 35)
print(e1)
print(e2.display_salary())
print(e2.calculate_age_(15))
print("###########################################")
#
# Create a class for a fruits so it will have weight, color and days old. Make sure you have a fucntion which
# returns information about fruit. And make sure you when you add quantity of apple it will calculate total size of
# whole bag.

class fruits:
    def __init__(self, name, weight, old_days, color):
        self.name = name
        self.weight = weight
        self.old_days = old_days
        self.color = color

    def display(self):
        return f"{self.name} is {self.color}, weight is {self.weight}lb and {self.old_days} days old."

    def calculate_total_weight(self, count):
        return f"In my bag {count} {self.name}s and total weight is {self.weight * count}lb"


f1 = fruits("apple", 2, 4, "red")
print(f1.display())
print(f1.calculate_total_weight(10))


