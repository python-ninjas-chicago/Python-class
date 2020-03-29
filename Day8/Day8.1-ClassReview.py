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
#



