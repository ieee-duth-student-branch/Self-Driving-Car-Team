import keyboard as kb
import car

kb.init()

if kb.getKey("UP"):
    car.Forward(100, 0.1)
elif kb.getKey("DOWN"):
    car.Backward(100, 0.1)
elif kb.getKey("RIGHT"):
    car.Right(100, 0.1)
elif kb.getKey("LEFT"):
    car.Left(100, 0.1)
else:
    car.Stop(0.1)
