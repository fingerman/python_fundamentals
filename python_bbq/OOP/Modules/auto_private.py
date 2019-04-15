class AutoPrivate:
    def __init__(self, speed=0):      # self is the current object/instance
        self.__speed = speed          # both speeds are different things. Second speed is the value of speed

    def speed_up(self, speed):
        self.__speed += speed
        return self.__speed


# cannot give -  car.speed

car = AutoPrivate(5)
print(car._AutoPrivate__speed)




'''
_speed     - private attribute
__speed     - extreamly private attribute



'''




