class Auto:
    def __init__(self, speed=0):      # self is the current object/instance
        self.speed = speed          # both speeds are different things. Second speed is the value of speed

    def speed_up(self, speed):
        self.speed += speed


car = Auto(5)
car.speed_up(10)
print(car.speed)
