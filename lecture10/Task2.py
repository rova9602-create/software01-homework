class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def set_speed(self, speed):
        # 最大速度を超えないように制限
        if speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


# main program
electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

# speeds
electric.set_speed(150)
gasoline.set_speed(140)

# drive 3 hours
electric.drive(3)
gasoline.drive(3)

# print results
print(f"Electric Car distance: {electric.travelled_distance} km")
print(f"Gasoline Car distance: {gasoline.travelled_distance} km")
