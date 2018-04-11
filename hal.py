import mcp3008
import time
import os
import temp_convert as tc
if os.name == 'posix':
    import RPi.GPIO as GPIO
    print("USE: ORIGINAL GPIO")
else:
    import mock as GPIO
    print("USE: MOCK GPIO")

GPIO.setmode(GPIO.BCM)
# Heating relay
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
# Pump relay
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
    #global temp_debug
    #print("get t'=>", temp_debug)
    tarr = []
    i = 0
    while i < 100:
        i = i + 1
        tarr.append(mcp3008.get_temp())
        time.sleep(0.01)

    return tc.convert_to_celsius(sum(tarr)/len(tarr))


def set_temp(temp):
    global temp_debug
    temp_debug = temp


