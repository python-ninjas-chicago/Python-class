class Temperature:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def display_cel_to_f(self, count):
        return f"Today's temperature is {count * 9/5 + 32} {self.fahrenheit}"

    def display_fahr_to_c(self, count):
        return f"Today's temperature is {(count - 32) * 5/9} {self.celsius}"

c = Temperature('celsius', 'fahrenheit')
print(c.display_cel_to_f(10))
print(c.display_fahr_to_c(50))
