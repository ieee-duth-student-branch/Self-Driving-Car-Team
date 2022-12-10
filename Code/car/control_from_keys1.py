import keyboard as kb
from car1 import car

kb.init()
my_car = car(2, 3, 4, 17, 27, 22)

if kb.getKey("UP"):
    my_car.move(1, 0, 0.1)
elif kb.getKey("DOWN"):
    my_car.move(-1, 0, 0.1)
elif kb.getKey("RIGHT"):
    my_car.move(0, 1, 0.1)
elif kb.getKey("LEFT"):
    my_car.move(0, -1, 0.1)
else:
    my_car.stop(0.1)
