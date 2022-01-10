# 문제 풀이2

# 라즈베리 파이 보드 GPIO 18번 핀으로 제어하는 LED 회로 구성

# 숫자 0 누르면 LED 밝기 0
# 숫자 5 누르면 LED 밝기 50%
# T 누르면 100%로 조절하기

# PWM활용
# Pwm.ChangeDutyCycle()

import RPi.GPIO as GPIO

led_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 1000.0)
pwm.start(0.0)

try:
    while True:
        userInput = input()
        if userInput == '0':
          pwm.ChangeDutyCycle(0)
        elif userInput == '5':
          pwm.ChangeDutyCycle(50)
        elif userInput == 'T':
          pwm.ChangeDutyCycle(100)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
