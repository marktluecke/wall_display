p = 10
from gpiozero import LED
from time import sleep

g = LED(p)
g.on()
sleep(8)
g.off()
