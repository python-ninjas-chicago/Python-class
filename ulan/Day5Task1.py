def add_car(cars, item):
    brand, model = item.split(":")##Alternative options "pair = item.split(":")"
    cars[brand] = model ##Alternative options "cars[pair[0]] = pair[1]"  ###"Toyota : camry"
my_cars = dict()
while True:
    item = input("Please enter your car: ")
    if item == "moskvich":
       break
    add_car(my_cars, item)
print(my_cars)
