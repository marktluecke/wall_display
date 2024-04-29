from flask import Flask, render_template, request, redirect
from display import display as d
from gpiozero import RGBLED, Button
import threading
import logging
import board
import neopixel
from time import sleep



led = RGBLED(red=10, green=14, blue=15)
button = Button(2)
siren_leds = 12

disp_unit_1 = d.DispUnit(4,16,23,20,9,27,21,22)
disp_unit_2 = d.DispUnit(1,25,17,7,8,3,24,12)
disp = d.Display([disp_unit_1,disp_unit_2])
pixels = neopixel.NeoPixel(board.D18, sirene_leds, brightness = 1)
pixels.fill((0, 0, 0))

app = Flask(__name__)

number = 0

@app.route("/disp", methods=['GET', 'POST'])
def index():
    global number
    message = "Display your number"

    if request.method == 'POST':
        if request.form.get('add_one') == '+1':
            print("+1")
            number += 1
            pass
        elif request.form.get('add_five') == '+5':
            print('+5')
            number += 5
            pass
        elif request.form.get('sub_one') == '-1':
            print('-1')
            number -= 1
            pass
        elif request.form.get('sub_five') == '-5':
            print('-5')
            number -= 5
            pass
        else:
            pass

        num = request.form.get('count')
        if num is not None:
            number = int(num)
        print(num)

    elif request.method == 'GET':
#        return(render_template('index.html', message=message))
        pass


    if number < 0:
        number = 0
    elif number > 99:
        number = 99

    disp.dispNumber(number)

    return(render_template('disp.html', message=message, done_today=number))


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'POST':
        if request.form['button'] == 'call':
            for n in range(10):
                for p in range(led_count):
                    pixels[p] = (255, 0, 0)
                    pixels[p-5] = (0, 0, 0)
                    sleep(0.03)
            pixels.fill((0, 0, 0))
        else:
            pass
    return render_template('index.html')


def button_control():
    global number
    while(True):
        button.wait_for_press()
#        number += 1
        print('button pressed')

if __name__ == '__main__':
#	app.run(debug=True, host="0.0.0.0")
    threading.Thread(target=lambda: app.run(host="0.0.0.0", debug=True, use_reloader=False)).start()
    threading.Thread(target=button_control).start()
