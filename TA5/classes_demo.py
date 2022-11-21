class employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary


e = employee("Bill", 100)
# protected
print(e._name)
print(e._salary)
print("________________________________________________________________________________")
print("________________________________________________________________________________")


class employee2:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary


e2 = employee2("Dan", 500)
# private -> can we access a private modifier???
# print(e2.__name)
# print(e2.__salary)
print("________________________________________________________________________________")
print("________________________________________________________________________________")


class Car:
    # pass
    def __init__(self, plate_number, year, hp):
        self.plate_number = plate_number
        self.year = year
        self.hp = hp

    def __str__(self):
        return f'Car ->(plate number: {self.plate_number}, year: {self.year}, horse power: {self.hp})'


class Ford(Car):
    def __init__(self, plate_number, year, hp, model, price):
        super().__init__(plate_number, year, hp)
        self.model = model
        self.price = price

    def __str__(self):
        return super().__str__()[:-1] + f', model: {self.model}, price: {self.price})'


c = Car(11111, 2020, 100)
# a = [c for _ in range(10)]
print(c)

f = Ford(22222, 2019, 120, "Focus", 120000)
print("Ford method ->", f)
print("Car method ->", super(type(f), f).__str__())


