import gpiozero as gpio
import time

led = gpio.LED(6, active_high=False, initial_value=0)

def dit():
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)

def dah():
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.1)

def send_s():
    dit()
    dit()
    dit()
    time.sleep(0.2)

def send_o():
    dah()
    dah()
    dah()
    time.sleep(0.2)

while True:
    send_s()
    send_o()
    send_s()
    time.sleep(0.4)
