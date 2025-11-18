class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, destination):
        elevator = self.elevators[number]
        elevator.go_to_floor(destination)

    def fire_alarm(self):
        print("FIRE ALARM! All elevators return to bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)
