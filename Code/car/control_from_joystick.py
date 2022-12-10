import joystick as js
from car1 import car

js_value = js.getJS()
my_car = car(2, 3, 4, 17, 27, 22)

my_car.move(js_value['axis_2'], js_value['axis_1'], 0.1)
