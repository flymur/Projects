from __future__ import print_function
#Stop light code
import RPi.GPIO as GPIO
import time
import keyboard
import sys

def red(light, sec):
	GPIO.output(light,True)
	print("Red light is on")
	while sec:		
		if keyboard.is_pressed('enter'):
                        walk(4,17,10)
			break
		if sec < 1:
			break
		tformat = '{:02d}'.format(sec)
		print(tformat, end='\r')
		sys.stdout.flush()
                time.sleep(1)
		sec -= 1
		
	turnOffLight(light,.1)
	green(27, 10)
	
def green(light, sec):
	GPIO.output(light,True)
	print("Green light is on")
	while sec:
		if keyboard.is_pressed('enter'):
			continueGreen(sec)
			break
		if sec < 1:
			break
		tformat = '{:02d}'.format(sec)
		print(tformat, end='\r')
		sys.stdout.flush()
		time.sleep(1)
		sec -= 1
				
	turnOffLight(light,.1)
	amber(17,5)
	
def amber(light, sec):
	GPIO.output(light,True)
	print("Amber light is on")
	while sec:
		if keyboard.is_pressed('enter'):
			continueAmber(sec)
			break
		if sec < 1:
			break
		tformat = '{:02d}'.format(sec)
		print(tformat, end='\r')
		sys.stdout.flush()
		time.sleep(1)
		sec -= 1
		
	turnOffLight(light,.1)
	red(4,10)
	
def walk(light1, light2, sec):
	GPIO.output(light1, True)
	GPIO.output(light2, True)
	print("It is safe to walk")
	while sec:
		tformat = '{:02d}'.format(sec)
		print(tformat, end='\r')
		sys.stdout.flush()
		time.sleep(1)
		sec -= 1
		
	turnOffBothLights(light1,light2,.1)
	green(27,10)
	
def continueGreen(sec):
        print("Continuing green")
	while sec:
		tformat = '{:02d}'.format(sec)
		print(tformat, end='\r')
		sys.stdout.flush()
		time.sleep(1)
		sec -= 1
		
	turnOffLight(27,.1)	
	amber2(17,5)
	
def continueAmber(sec):
        print("Continuing amber")
	while sec:
		tformat = '{:02d}'.format(sec)
		print(tformat, end='\r')
		sys.stdout.flush()
		time.sleep(1)
		sec -= 1
		
	turnOffLight(17,.1)	
	walk(4,17,10)
	
def amber2(light, sec):
	GPIO.output(light,True)
	print("In amber to go to walk")
	while sec:
		tformat = '{:02d}'.format(sec)
		print(tformat, end='\r')
		sys.stdout.flush()
		time.sleep(1)
		sec -= 1
		
	turnOffLight(light,.1)
	walk(4,17,10)
	
def turnOffLight(light, sec):
	GPIO.output(light, False)
	time.sleep(sec)
	print("light is off\n")
	return
	
def turnOffBothLights(light1, light2, sec):
	GPIO.output(light1, False)
	GPIO.output(light2, False)
	time.sleep(sec)
	print("Red and Amber lights are off\n")
	return

def start():

        red(4,10)
		
#Setting up the chip	
GPIO.setmode(GPIO.BCM)

#setting up the pins via their number on the bread board
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
		
start()
GPIO.cleanup()
