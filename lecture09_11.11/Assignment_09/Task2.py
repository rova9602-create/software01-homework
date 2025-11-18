class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def floor_up(self):
        if self.floor < self.top:
            self.floor += 1
            print(f"Elevator is now at floor {self.floor}")

    def floor_down(self):
        if self.floor > self.bottom:
            self.floor -= 1
            print(f"Elevator is now at floor {self.floor}")

    def go_to_floor(self, target):
        while self.floor < target:
            self.floor_up()
        while self.floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, destination):
        elevator = self.elevators[number]
        elevator.go_to_floor(destination)


b = Building(1, 10, 3)

b.run_elevator(0, 7)
b.run_elevator(2, 3)
