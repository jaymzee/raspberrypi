import gpiozero as gpio
from flask import Flask, request, jsonify, abort

app = Flask(__name__)
leds = {
    'blue': gpio.LED(6, active_high=False),
    'red':  gpio.LED(13, active_high=False),
    'green': gpio.LED(19, active_high=False),
    'yellow': gpio.LED(26, active_high=False)
}

@app.route('/leds/')
def get_leds():
    return jsonify({'leds': list(leds.keys())})

@app.route('/leds/<string:name>')
def get_led(name):
    if name not in leds:
        abort(404)
    return jsonify({'active': leds[name].value != 0})

@app.route('/leds/<string:name>', methods=['PUT'])
def set_led(name):
    if name not in leds:
        abort(404)
    led = leds[name]
    if request.json['active']:
        led.value = 1
    else:
        led.value = 0
    return jsonify({'active': led.value != 0})

@app.route('/')
def index():
    return 'led server'
