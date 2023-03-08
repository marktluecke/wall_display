from gpiozero import LED
from time import sleep

class Display:
    def __init__(self, pin_point, pin_up, pin_up_left, pin_up_right, pin_middle, pin_down_left, pin_down_right, pin_down):
        self.led_point = LED(pin_point)
        self.led_up = LED(pin_up)
        self.led_up_left = LED(pin_up_left)
        self.led_up_right = LED(pin_up_right)
        self.led_middle = LED(pin_middle)
        self.led_down_left = LED(pin_down_left)
        self.led_down_right = LED(pin_down_right)
        self.led_down = LED(pin_down)

        self.zero = [[1],[1,1],[0],[1,1],[1],[0]]
        self.one = [[0],[0,1],[0],[0,1],[0],[0]]
        self.two = [[1],[0,1],[1],[1,0],[1],[0]]
        self.three = [[1],[0,1],[1],[0,1],[1],[0]]
        self.four = [[0],[1,1],[1],[0,1],[0],[0]]
        self.five = [[1],[1,0],[1],[0,1],[1],[0]]
        self.six = [[1],[1,0],[1],[1,1],[1],[0]]
        self.seven = [[1],[0,1],[0],[0,1],[0],[0]]
        self.eight = [[1],[1,1],[1],[1,1],[1],[0]]
        self.nine = [[1],[1,1],[1],[0,1],[1],[0]]

        self.all_on = [[1],[1,1],[1],[1,1],[1],[1]]
        self.all_off = [[0],[0,0],[0],[0,0],[0],[0]]

        self.digits = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]

    def ledTest(self):
        self.reset(True)
        sleep(10)
        self.reset(False)
        sleep(2)
        self.reset(True)
        sleep(1)
        self.reset(False)


    def reset(self, status: bool):
        if status:
            self.dispMatrix(self.all_on)

        if not status:
            self.led_point.off()
            self.led_up.off()
            self.led_up_left.off()
            self.led_up_right.off()
            self.led_middle.off()
            self.led_down_left.off()
            self.led_down_right.off()
            self.led_down.off()


    def dispDigit(self, digit):
        self.reset()
        self.dispMatrix(self.digits[digit])


    def dispMatrix(self, matrix):
        if matrix[0][0] == 1:
            self.led_up.on()

        if matrix[1][0] == 1:
            self.led_up_left.on()

        if matrix[1][1] == 1:
            self.led_up_right.on()

        if matrix[2][0] == 1:
            self.led_middle.on()

        if matrix[3][0] == 1:
            self.led_down_left.on()

        if matrix[3][1] == 1:
            self.led_down_right.on()

        if matrix[4][0] == 1:
            self.led_down.on()

        if matrix[5][0] == 1:
            self.led_point.on()





def loopDigits():
    n = 0
    while(True):
        n = 0
        while(n <= 9):
            disp.dispDigit(n)
            n += 1
            sleep(1)


disp = Display(2,22,3,10,4,17,9,27)

disp.ledTest()
