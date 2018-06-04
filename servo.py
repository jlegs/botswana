import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

center = 7.5
left = 12
right = 4
delay = 1
initdelay = 0.05
servo_pin = 12
freq = 50 

GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
time.sleep(initdelay)
mypwm = GPIO.PWM(servo_pin,freq)
pwm = GPIO.PWM(35,freq)

print('Initialized PWM pin 12 at 50 Hertz')
mypwm.start(center)
time.sleep(.5)
pwm.start(center)
print('Started duty cycle at center postion')
time.sleep(delay)
mypwm.ChangeDutyCycle(left)
time.sleep(.5)
pwm.ChangeDutyCycle(left)
print('change duty cycle to left position')
time.sleep(delay)
mypwm.ChangeDutyCycle(right)
time.sleep(.5)
pwm.ChangeDutyCycle(right)
print('change duty cycle to right postion')
time.sleep(delay)

GPIO.cleanup()
