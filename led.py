import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, GPIO.HIGH)
time.sleep(2)
GPIO.output(19, GPIO.LOW)
GPIO.cleanup()

