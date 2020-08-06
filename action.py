from gpiozero import Button
from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)
vibro = PWMLED(17)
button = Button(2)

def action():
    for i in range(3):
        led.value = 1
        sleep(0.2)
        led.value = 0.25
        sleep(1)
        led.value = 1
        sleep(0.2)
        led.value = 0.25
        sleep(1)
    led.value = 0
