import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
left = 11
right = 4
center = 7

freq = 50

GPIO.setup(12, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

pwm1 = GPIO.PWM(12, freq)
pwm2 = GPIO.PWM(35, freq)

pwm1.start(right)
pwm2.start(right)
time.sleep(.2)

def stepup(pwm1, pwm2):
    time.sleep(.3)
    pwm1.ChangeDutyCycle(3)
    pwm2.ChangeDutyCycle(3)

def stepdown(pwm1, pwm2):
    time.sleep(.3)
    pwm1.ChangeDutyCycle(5)
    pwm2.ChangeDutyCycle(6)


def fullstep(pwm1, pwm2):
    stepup(pwm1, pwm2)
    stepdown(pwm1, pwm2)

#inp = raw_input('>>')

#while inp != 's':
#    print 'x'


fullstep(pwm1, pwm2)
fullstep(pwm1, pwm2)
fullstep(pwm1, pwm2)
fullstep(pwm1, pwm2)
fullstep(pwm1, pwm2)


GPIO.cleanup()



