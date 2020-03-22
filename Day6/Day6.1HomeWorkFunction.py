def add_car(car_dict, entries):
    brand, model = entries.split()
    car_dict[brand] = model
    #entries = entries.split()
    #car_dict[entries[0]] = entries[1]


cars = {}  # cars = dict()

while True:
    car_info = input("Enter car: ")
    if car_info == "done":
        break
    else:
        add_car(cars, car_info)
print(cars)