# A 누르면 전진
# S 누르면 후진
# D 누르면 정지

# 코드 만들기
import RPi.GPIO as GPIO
import time

B_IA_pwm = 18
B_IB = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(B_IA_pwm,GPIO.OUT)
GPIO.setup(B_IB, GPIO.OUT)

pwm = GPIO.PWM(B_IA_pwm, 1000.0)
pwm.start(0.0)

try:
  while True:
    userInput = input()
    if userInput == 'a' or userInput == 'A':
      GPIO.output(B_IB, True)
      pwm.ChangeDutyCycle(0.0)
      time.sleep(1.0)
    if userInput == 's' or userInput == 'S':
      GPIO.output(B_IB, False)
      pwm.ChangeDutyCycle(100.0)
      time.sleep(1.0)
    if userInput == 'd' or userInput == 'D':
      GPIO.output(B_IB, False)
      pwm.ChangeDutyCycle(0.0)
      time.sleep(1.0)
except KeyboardInterrupt:
  pass

pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()
