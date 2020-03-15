person1 = input("Please enter first person: ")
person2 = input("Please enter second person: ")

person1 = person1.split(", ")
person2 = person2.split(", ")

person1dict = {"name": person1[0], "age": int(person1[1]), "salary": int(person1[2]), "city": person1[3]}
person2dict = {"name": person2[0], "age": int(person2[1]), "salary": int(person2[2]), "city": person2[3]}

if person1dict["salary"] > person2dict['salary']:
    print("{0} has higher salary, which is {1}. His/her age {2}".format(person1dict["name"], person1dict["salary"], person1dict["age"]))
else:
    print("{0} has higher salary, which is {1}. His/her age {2}".format(person2dict["name"], person2dict["salary"], person2dict["age"]))
