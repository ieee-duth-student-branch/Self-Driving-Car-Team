from car1 import car
# Define Gpio pins
my_car = car(2, 3, 4, 17, 27, 22)

# Forward
my_car.move(1, 0, 2)
my_car.stop(2)
# Backward
my_car.move(-1, 0, 2)
my_car.stop(2)
# Right
my_car.move(0, 1, 2)
my_car.stop(2)
# Left
my_car.move(0, -1, 2)
my_car.stop(2)
