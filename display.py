from gpiozero import LED
from time import sleep

class Display:
        def __init__(self, pin_point, pin_up, pin_up_left, pin_up_right, pin_middle, pin_down_left, pin_down_right, pin_down):
                self.pin_point = LED(pin_point)
                self.pin_up = LED(pin_up)
                self.pin_up_left = LED(pin_up_left)
                self.pin_up_right = LED(pin_up_right)
                self.pin_middle = LED(pin_middle)
                self.pin_down_left = LED(pin_down_left)
                self.pin_down_right = LED(pin_down_right)
                self.pin_down = LED(pin_down)

	
	def ledTest():
		self.pin_point.on()
                self.pin_up.on()
                self.pin_up_left.on()
                self.pin_up_right.on()
                self.pin_middle.on()
                self.pin_down_left.on()
                self.pin_down_right.on()
                self.pin_down.on()
		
		sleep(5)
		
		self.pin_point.off()
                self.pin_up.off()
                self.pin_up_left.off()
                self.pin_up_right.off()
                self.pin_middle.off()
                self.pin_down_left.off()
                self.pin_down_right.off()
                self.pin_down.off()
		
		
Display(2,3,4,17,27,22,10,9)
