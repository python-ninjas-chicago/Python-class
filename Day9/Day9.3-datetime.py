from datetime import datetime

x = datetime.now()
print(x)

print(x.year)
print(x.strftime("%A, %d %B %Y %I:%M"))

y = datetime(2020, 5, 18)
print(y)