from gpiozero import RGBLED
from time import sleep
led = RGBLED(red=26, green=19, blue=13)

duration = 2

for n in range(100):
    led.blue = n/100
    led.red = n/100
    led.green = n/100
    sleep(0.05)
    led.color = (0, 0, 0) # off
    sleep(duration)
    led.red = 1 # full red
    sleep(duration)
    led.red = 0.5 # half red
    sleep(duration)
    led.color = (1, 1, 0) # yellow
    sleep(duration)
    led.color = (0, 1, 0) # full green
    sleep(duration)
    led.color = (0, 1, 1) # cyan
    sleep(duration)
    led.color = (0, 0, 1) # full blue
    sleep(duration)
    led.color = (1, 0, 1) # magenta
    sleep(duration)
    led.color = (1, 1, 1) # white
    sleep(duration)
    led.color = (0, 0, 0) # off

