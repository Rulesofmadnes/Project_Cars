import random


class Car:
    def __init__(self, car_model, car_color, car_economy, mileage=0, fuel=100):
        self.model = car_model
        self.color = car_color
        self.economy = car_economy
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, distance):
        fuel_needed = distance / self.economy
        if fuel_needed > self.fuel:
            print("Ошибка: не хватает топлива!")
        else:
            self.mileage += distance
            self.fuel -= fuel_needed

    def distance_left(self):
        return (f"Машина {self.model} может проехать "
                f"{self.fuel * self.economy} км с учетом текущего запаса топлива.")

    def fuel_up(self):
        self.fuel += 20


models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
cars = []
for _ in range(10):
    model = random.choice(models)
    color = random.choice(["красный", "синий", "зеленый", "желтый", "черный"])
    economy = random.randint(5, 15)
    car = Car(car_model=model, car_color=color, car_economy=economy)
    cars.append(car)

for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

max_fuel_car = max(cars, key=lambda x: x.fuel)
print(f"Машина с наибольшим запасом топлива: {max_fuel_car.model}, "
      f"{max_fuel_car.color}, пробег: {max_fuel_car.mileage} км, "
      f"остаток топлива: {max_fuel_car.fuel}")
