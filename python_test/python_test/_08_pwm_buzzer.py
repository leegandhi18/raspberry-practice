import RPi.GPIO as GPIO
import time

buzzer_pin=18

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer_pin,GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 262)
pwm.start(50.0)

time.sleep(2.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()