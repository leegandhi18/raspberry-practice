import RPi.GPIO as GPIO
import time

B_IA_pwm = 18
B_IB = 17

B_IA_pwm2 = 16
B_IB2 = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(B_IA_pwm, GPIO.OUT)
GPIO.setup(B_IB, GPIO.OUT)
GPIO.setup(B_IA_pwm2, GPIO.OUT)
GPIO.setup(B_IB2, GPIO.OUT)

pwm = GPIO.PWM(B_IA_pwm, 1000.0)
pwm2 = GPIO.PWM(B_IA_pwm2, 1000.0)
pwm.start(0.0)
pwm2.start(0.0)

try:
  while True:
    GPIO.output(B_IB, False)
    GPIO.output(B_IB2, False)
    pwm.ChangeDutyCycle(0.0)
    pwm2.ChangeDutyCycle(0.0)
    time.sleep(1.0)
    
    GPIO.output(B_IB, True)
    GPIO.output(B_IB2, True)
    pwm.ChangeDutyCycle(0.0)
    pwm2.ChangeDutyCycle(0.0)
    time.sleep(1.0)

    GPIO.output(B_IB, True)
    GPIO.output(B_IB2, True)
    pwm.ChangeDutyCycle(100.0)
    pwm2.ChangeDutyCycle(100.0)
    time.sleep(1.0)

    GPIO.output(B_IB, False)
    GPIO.output(B_IB2, False)
    pwm.ChangeDutyCycle(100.0)
    pwm2.ChangeDutyCycle(100.0)
    time.sleep(1.0)
except KeyboardInterrupt:
  pass

pwm.ChangeDutyCycle(0.0)
pwm.stop()
GPIO.cleanup()