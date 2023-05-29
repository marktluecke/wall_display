from flask import Flask, render_template, request, redirect
from display import display as d
from gpiozero import RGBLED, Button

led = RGBLED(red=18, green=14, blue=15)
button = Button(2)

disp_unit_1 = d.DispUnit(4,16,23,20,10,27,21,22)
disp_unit_2 = d.DispUnit(1,25,17,7,8,3,24,12)
disp = d.Display([disp_unit_1,disp_unit_2])

app = Flask(__name__)

@app.route("/")
def index():
    message = "Display your number"
    return(render_template('index.html', message=message))

@app.route("/", methods=('GET', 'POST'))
def create():
    message = "Test"

    print(request.form['title'])
    disp.dispNumber(request.form['title'])
    return(redirect("/"))

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")

