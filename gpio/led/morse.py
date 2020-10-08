import gpiozero as gpio
import time
import sys

morse_lu = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

def dit(led):
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)

def dah(led):
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.1)

def send_char(led, c):
    code = morse_lu[c]
    for i in code:
        if i == ".":
            dit(led)
        elif i == "-":
            dah(led)
        else:
            raise ValueError()
    time.sleep(0.2)

def send_msg(led, msg):
    for c in msg.upper():
        if c == " ":
            time.sleep(0.4)
        elif c == ".":
            time.sleep(1.0)
        else:
            send_char(led, c)

def main():
    blue = gpio.LED(6, active_high=False, initial_value=0)
    while True:
        if len(sys.argv) == 2:
            send_msg(blue, sys.argv[1])
        else:
            send_msg(blue, 'Hello world ')


if __name__ == '__main__':
    main()
