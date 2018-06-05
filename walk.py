import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
left = 11
right = 2.5
center = 7

freq = 50
time.sleep(2)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

pwm1 = GPIO.PWM(12, freq)
pwm2 = GPIO.PWM(35, freq)

pwm1.start(3.5)
pwm2.start(3.5)


time.sleep(1)

def stepup(pwm1, pwm2):
    time.sleep(.3)
    pwm1.ChangeDutyCycle(4)
    pwm2.ChangeDutyCycle(4)

def stepdown(pwm1, pwm2):
    time.sleep(.3)
    pwm1.ChangeDutyCycle(5)
    pwm2.ChangeDutyCycle(5)


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
fullstep(pwm1, pwm2)
fullstep(pwm1, pwm2)
fullstep(pwm1, pwm2)


GPIO.cleanup()



