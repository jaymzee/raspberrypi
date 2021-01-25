import gpiozero as gpio
from flask import Flask, jsonify, abort

app = Flask(__name__)
leds = {
    'blue': gpio.LED(6, active_high=False),
    'red':  gpio.LED(13, active_high=False),
    'green': gpio.LED(19, active_high=False)
}

@app.route('/leds')
def get_leds():
    return jsonify({ 'leds': list(leds.keys()) })

@app.route('/leds/<string:name>')
def get_led(name):
    if name not in leds:
        abort(404)
    resp = jsonify({'active': leds[name].value != 0})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/leds/<string:name>/<int:value>', methods=['PUT'])
def set_led(name, value):
    if name not in leds:
        abort(404)
    led = leds[name]
    led.value = value
    resp = jsonify({'active': led.value != 0})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/')
def index():
    return 'led server'
