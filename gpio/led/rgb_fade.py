import gpiozero as gpio

ledb = gpio.PWMLED(6)
ledr = gpio.PWMLED(13)
ledg = gpio.PWMLED(19)

ledb.blink(fade_in_time=2.0, fade_out_time=2.0)
ledr.blink(fade_in_time=1.0, fade_out_time=1.0)
ledg.blink(fade_in_time=0.5, fade_out_time=0.5, background=False)
