#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def led_on():
    pin_num = int(input("which pin are we working with?: "))
    GPIO.setup(pin_num, GPIO.OUT)
    print("Turning on pin number {}".format(pin_num))
    GPIO.output(pin_num, GPIO.HIGH)


def led_off():
    pin_num = int(input("which pin are we working with?: \n"))
    GPIO.setup(pin_num, GPIO.OUT)
    print("Turning off pin number {}".format(pin_num))
    GPIO.output(pin_num, GPIO.LOW)


fin = "n"
while fin == "n":
    choice = input("What would you like to do? You can either turn an LED on, or turn an LED off. on/off")
    if choice == "on":
        led_on()
        fin = input("are you done?: Y/n \n")

    if choice == "off":
        led_off()
        fin = input("are you done?: Y/n? \n")
    else:
        print("")
