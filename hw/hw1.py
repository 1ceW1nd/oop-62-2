class Car:
    def __init__(self, brand, speed, fuel):
        self.brand = brand
        self.speed = speed
        self.fuel = fuel

    def get_info(self):
        return "Марка: " + self.brand + ", Скорость: " + str(self.speed) + " км/ч, Топливо: " + str(self.fuel)

    def accelerate(self):
        self.speed += 10
        return "Скорость увеличена. Текущая скорость: " + str(self.speed)


car1 = Car("Toyota", 60, 50)
car2 = Car("BMW", 80, 40)

print(car1.get_info())
print(car1.accelerate())

print(car2.get_info())
print(car2.accelerate())