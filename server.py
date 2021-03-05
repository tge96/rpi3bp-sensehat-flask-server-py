from sense_hat import SenseHat
import time
import requests # sudo apt-get install python-requests
sense = SenseHat()
degree_symbol = u"\N{DEGREE SIGN}"

from flask import Flask #sudo pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

@app.route("/temperature")
def temperature():
	t = sense.get_temperature() * (9/5) + 32 # convert to degrees F
	t = str(round(t, 1)) # convert to string
	temperature_now = 'Temperature ' + t + degree_symbol + ' recorded at ' + time.strftime("%H:%M:%S", time.localtime())
	return temperature_now

@app.route("/humidity")
def humidity():
	h = sense.get_humidity()
	h = str(round(h, 1))
	humidity_now = 'Humidity ' + h + '% recorded at ' + time.strftime("%H:%M:%S", time.localtime())
	return humidity_now

@app.route("/pressure")
def pressure():
	p = sense.get_pressure() / 33.864 # convert to inHg (inches of mercury)
	p = str(round(p, 1))
	pressure_now = 'Pressure ' + p + 'inHg recorded at ' + time.strftime("%H:%M:%S", time.localtime())
	return pressure_now

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True) 
