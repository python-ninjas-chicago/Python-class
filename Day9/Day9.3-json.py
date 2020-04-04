import json
# Converting string to json
x = '{"name": "Thomas", "age":15, "city":"Chicago"}'
y = json.loads(x)

print(y["name"], y["age"])
print("=============================================")
# Converting dictinary to json
z = {
    "name": "Tim",
    "age": 20,
    "city": "Miami"
}
print(type(z))

g = json.dumps(z)
print(z)
print("==============================================")


