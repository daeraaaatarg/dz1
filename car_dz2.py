class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(f"This car's make is {self.make}")
        print(f"The model is {self.model}")
        print(f"The year of production is {self.year}")

    def get_info_return(self):
        return f"{self.year} {self.make} {self.model}"

Peugeot = Car("Peugeot", "308 SW", "2010")
Peugeot.get_info()
print("--------------------------------")
MyPeugeot = Car("Peugeot", "308 SW", 2010)
print(MyPeugeot.get_info_return())