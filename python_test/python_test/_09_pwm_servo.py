import RPi.GPIO as GPIO
import time

servo_pin=18

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50) # 50Hz
pwm.start(3.0) # 0.6ms

time.sleep(2.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()