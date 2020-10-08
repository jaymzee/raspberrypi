import gpiozero as gpio

ledb = gpio.LED(6)
ledr = gpio.LED(13)
ledg = gpio.LED(19)
ledy = gpio.LED(26)

ledy.blink(on_time=0.5, off_time=0.5)
ledb.blink(on_time=0.25, off_time=0.25)
ledr.blink(on_time=0.125, off_time=0.125)
ledg.blink(on_time=0.0625, off_time=0.0625, background=False)
