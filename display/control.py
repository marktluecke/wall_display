from gpiozero import LED, Button
from time import sleep

led_red = LED(26)
led_green = LED(19)
button_left = Button(13)
button_right = Button(6)
button_switch = Button(5)

led_red.on()
led_green.on()

sleep(5)
