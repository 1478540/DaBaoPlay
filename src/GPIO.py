import RPi.GPIO as GPIO

def initialGPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

def overGPIO():
	GPIO.cleanup()