from gpiozero import LED
from time import sleep

class Display:
        def __init__(self, pin_point, pin_up, pin_up_left, pin_up_right, pin_middle, pin_down_left, pin_down_right, pin_down):
                self.pin_point = pin_point
                self.pin_up = pin_up
                self.pin_up_left = pin_up_left
                self.pin_up_right = pin_up_right
                self.pin_middle = pin_middle
                self.pin_down_left = pin_down_left
                self.pin_down_right = pin_down_right
                self.pin_down = pin_down

	
	def ledTest():

Display(2,3,4,17,27,22,10,9)
