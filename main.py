from flask import Flask, render_template, request, redirect
from display import display as d
from gpiozero import RGBLED

led = RGBLED(red=26, green=19, blue=13)

disp_unit_1 = d.DispUnit(2,22,3,10,4,17,9,27)
disp_unit_2 = d.DispUnit(7,24,14,25,15,18,8,23)
disp = d.Display([disp_unit_1, disp_unit_2])

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

