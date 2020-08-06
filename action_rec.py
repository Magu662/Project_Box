from gpiozero import Button
from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)
vibro = PWMLED(17)
button = Button(2)

def action():
    for i in range(2):
        led.value = 0.25
        vibro.value = 0
        sleep(0.2)
        led.value = 1
        vibro.value = 0.33
        sleep(1)
        led.value = 0.25
        vibro.value = 0
        sleep(0.2)
        led.value = 1
        vibro.value = 0.33
        sleep(1)
        led.value = 0.25
        vibro.value = 0
    for i in range(2):
        led.value = 1
        sleep(0.2)
        led.value = 0.25
        sleep(1)
        led.value = 1
        sleep(0.2)
        led.value = 0.25
        sleep(1)
    led.value = 0
while True:
        button.when_pressed = action



