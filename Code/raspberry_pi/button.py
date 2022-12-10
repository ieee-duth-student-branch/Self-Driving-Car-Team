from gpiozero import Button
from time import sleep

button = Button(2)

while True:
    sleep(0.5)
    if button.is_pressed:
        print("Button Pressed")
    else:
        print("Button Not Pressed")

# These don’t block the flow of the program
# button.when_pressed = led.on
# button.when_released = led.off
# Block the flow os the program
# button.wait_for_press()
# print("Pressed")
# button.wait_for_release()
# print("Released")