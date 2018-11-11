#!/usr/bin/python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json
from time import sleep

mqtt_broker="example.com"
#mqtt_broker="iot.eclipse.org"
state = "stop"
IN_A = 5 #GPIO:5
IN_B = 6 #GPIO:6

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/iot-plarail/eh200")
    return

def on_message(client, userdata, msg):
    value = json.loads(msg.payload)
    mode = value.get('mode')
    motor_mode(mode)
    return

def gpio_init():
        GPIO.setmode(GPIO.BMC)
        return


def gpio_cleanup():
        GPIO.cleanup()
        return

def motor_init():
        gpio_init()
        GPIO.setup(IN_A,GPIO.OUT)
        GPIO.setup(IN_B,GPIO.OUT)
        motor_stop()
        return

def motor_forward():
        GPIO.output(IN_A,GPIO.HIGH)
        GPIO.output(IN_B,GPIO.LOW)
        return

def motor_stop():
        GPIO.output(IN_A,GPIO.LOW)
        GPIO.output(IN_B,GPIO.LOW)
        return

def motor_mode(mode):
    state = mode

    print "mode: {0}".format(mode)

    if mode == "forward":
        motor_forward()
    elif mode == "stop":
        motor_stop()
    else:
        motor_stop() # fail safe
    return

def main():
        motor_init()
        motor_mode("stop")
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        try:
            client.connect(mqtt_broker, 1883, 300)
            client.loop_start()
            while True:
                sleep(5)
        except KeyboardInterrupt:
            print "exit"
            client.loop_stop()
            gpio_cleanup()

if __name__ == "__main__":
    main()
