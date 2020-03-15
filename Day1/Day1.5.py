import cmath, string, datetime


a = "Ulan is Cool developer"
b = "H is good letter"
print(a[3:6])
print(len(a))
print(a.strip())
print(b.strip("H"))
print(a.lower())
print(a.replace("Ulan", "Merim").strip())

print(a.split())
print(a.split()[2])

print("Here without colon <= " + a)
print(a + " " + b)

c = "Dina, is hard working"
print(c.split(","))