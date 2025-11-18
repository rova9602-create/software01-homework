class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom   # 最初は必ず最下階

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
