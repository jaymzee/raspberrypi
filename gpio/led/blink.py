import gpiozero as gpio

led = gpio.LED(6)

led.blink(on_time=0.5, off_time=0.5, background=False)
