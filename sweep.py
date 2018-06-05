import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
left = 4
right = 11

freq = 50

GPIO.setup(12, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
time.sleep(2)

pwm1 = GPIO.PWM(12, freq)
pwm2 = GPIO.PWM(35, freq)

pwm1.start(left)
pwm2.start(left)
time.sleep(.2)

def sweepup(pwm1, pwm2):
    for x in range(5, 11):
        print 'x is ', x
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        time.sleep(.3)

def sweepdown(pwm1, pwm2):
    for x in reversed(range(5, 11)):
        print 'x is ', x
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        time.sleep(.3)



sweepup(pwm1, pwm2)
sweepdown(pwm1, pwm2)

GPIO.cleanup()



