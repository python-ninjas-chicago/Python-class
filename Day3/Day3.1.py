
cars = {"brand":"Toyota", "model":"camry", "year": 2020}

print(cars)
#{'brand': 'Toyota', 'model': 'camry', 'year': 2020}

print(cars["model"])
#camry
print(cars["year"])
# 2020
x = cars.get("model")
print(x)
print(cars.get("model"))
# camry
cars["model"] = "avalon"
print(cars)
#{'brand': 'Toyota', 'model': 'avalon', 'year': 2020}
cars["engine"] = 2.5
print(cars)
#{'brand': 'Toyota', 'model': 'avalon', 'year': 2020, 'engine': 2.5}
print("=========================================")

for x, y in  cars.items():
    print(x, y)
#brand Toyota
#model avalon
#year 2020
#engine 2.5



if 'model' in cars:
    print("yes, model is in cars dictionary")
#yes, model is in cars dictionary

print(len(cars))
# 4

cars.pop("year")
print(cars)
#{'brand': 'Toyota', 'model': 'avalon', 'engine': 2.5}

cars.popitem()
print(cars)
#{'brand': 'Toyota', 'model': 'avalon'}

del cars['model']
print(cars)
#{'brand': 'Toyota'}

cars.clear()
print(cars)
#{}


