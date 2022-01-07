import RPi.GPIO as GPIO
import time

buzzer_pin=18

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer_pin,GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1.0)
pwm.start(50.0)

for cnt in range(0,3):
  pwm.ChangeFrequency(262)
  time.sleep(0.5)
  pwm.ChangeFrequency(294)
  time.sleep(0.5)

pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()