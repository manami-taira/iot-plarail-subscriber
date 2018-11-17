#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

IN_A = 20 #GPIO:20
IN_B = 21 #GPIO:21

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

def main():
	motor_init()
	motor_forward()
	time.sleep(2.0)
	motor_stop()
	gpio_cleanup()
	return

if __name__ == "__main__":
    main()

