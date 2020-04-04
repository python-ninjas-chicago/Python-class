#1)Create a Temprature class and two functions in class :
#Function 1 - takes celsius and convert to Fahrenheit.
#Function 2 - takes Fahrenheit and conver to Celsius.
#
#Use formula below to convert:
#celsius*9/5+32
#farenhiet-32*5/9


class Temperature:
    def __init__(self, fahrenheit, celsius):
        self.fahrenheit = fahrenheit
        self.celsius = celsius

    def convert_to_fahrenheit(self, temperature):
        return f'{temperature * 9 / 5 + 32} {self.fahrenheit}'

    def convert_to_celsius(self, temperature):
        print(f'{(temperature - 32) * 5 / 9} {self.celsius}')

temp = Temperature("fahrenheit", "celsius")

print(temp.convert_to_fahrenheit(20))
temp.convert_to_celsius(90)

print("==============================================")
#2)Replace __HERE__ with proper code.

import re
funny_url = "https://play.google.com/store/apps/details?id=com.microsoft.teams&hl=en_US%fake https://play.google.com/store/apps/details?id=com.spotify.music&hl=en_US%hi https://play.google.com/store/apps/details?id=com.yelp.android&hl=en_US$shell"
m = re.split("\s", funny_url)
m = re.search("^http.+US", m[0])
print(m.group())
#Result should be as:
#OUTPUT: https://play.google.com/store/apps/details?id=com.microsoft.teams&hl=en_US