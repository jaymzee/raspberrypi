import gpiozero as gpio

led = gpio.PWMLED(6, active_high=False)

led.blink(fade_in_time=0.2, 
          on_time=1.0, 
          fade_out_time=1.0,
          off_time=5.0, 
          background=False)
