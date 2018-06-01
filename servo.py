import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3, GPIO.OUT)
#GPIO.output(3, GPIO.HIGH)
#GPIO.setup(19, GPIO.OUT)
#GPIO.output(19, GPIO.HIGH)

GPIO.setup(12, GPIO.OUT)
mypwm = GPIO.PWM(12,50)
print('initialized pwm pin 12 at 50 somethings')

mypwm.start(0)
print('started duty cycle at 0')
time.sleep(2)
mypwm.ChangeDutyCycle(.002)
print('changed duty cycle to > 0')
time.sleep(2)
mypwm.ChangeDutyCycle(0)
print('chagne duty cycle is now 0')
time.sleep(2)




#time.sleep(1)
GPIO.cleanup()


