"""Inheritance patterns: specialization, extension, and super() usage."""

class Vehicle:
    def __init__(self, brand, *, wheels):
        self.brand = brand
        self.wheels = wheels

    def describe(self):
        return f"{self.brand} vehicle with {self.wheels} wheels"

    def honk(self):
        return "Generic horn sound"


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, wheels=4)
        self.model = model

    def describe(self):
        base_description = super().describe()
        return f"{base_description}; model {self.model}"

    def honk(self):
        return "Beep beep!"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity_kwh):
        super().__init__(brand, model)
        self.battery_capacity_kwh = battery_capacity_kwh

    def charging_time(self, power_kw):
        return self.battery_capacity_kwh / power_kw


class SirenMixin:
    def siren(self):
        return "WEE-OH WEE-OH"


class EmergencyElectricCar(SirenMixin, ElectricCar):
    def honk(self):
        # Emergency vehicles override the honk to use the siren.
        return self.siren()


def sound_check(vehicle):
    print(vehicle.describe())
    print("Honk:", vehicle.honk())


if __name__ == "__main__":
    fleet = [
        Vehicle("Generic", wheels=3),
        Car("Toyota", "Corolla"),
        Car("Toyota", "Corolla"),
        ElectricCar("Tesla", "Model 3", battery_capacity_kwh=75),
        ElectricCar("Tesla", "Model S", battery_capacity_kwh=75),
        EmergencyElectricCar("Rivian", "Responder", battery_capacity_kwh=120),
        EmergencyElectricCar("Rivian", "Responder", battery_capacity_kwh=120),
    ]

    for item in fleet:
        sound_check(item)
        if isinstance(item, ElectricCar):
            print("Charging time at 50 kW:", item.charging_time(50))
        print("-")
