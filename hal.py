import os
if os.name == 'posix':
    import RPi.GPIO as GPIO
    print("USE: ORIGINAL GPIO")
else:
    import mock as GPIO
    print("USE: MOCK GPIO")

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)


def switch_heating(state):
    if state:
        print("hot on")
        GPIO.output(20, GPIO.HIGH)
    else:
        print("hot off")
        GPIO.output(20, GPIO.LOW)


def switch_pump(state):
    if state:
        print("hot on")
        GPIO.output(21, GPIO.HIGH)
    else:
        print("hot off")
        GPIO.output(21, GPIO.LOW)


temp_debug = 999


def get_temp():
    global temp_debug
    print("get t'=>", temp_debug)
    return temp_debug


def set_temp(temp):
    global temp_debug
    temp_debug = temp
