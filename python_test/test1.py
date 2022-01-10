# 문제 풀이1

# 라즈베리 파이 보드 GPIO 17번 핀으로 제어하는 LED 회로 구성

# n,N키를 누르면 led가 켜지고
# f,F키를 누르면 led가 꺼지도록 만들어 보기
# While
# Input()
# If, elif
# Gpio setup output

import RPi.GPIO as GPIO

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        userInput = input()
        if userInput == 'n' or userInput == 'N':
          GPIO.output(led_pin, True)
        elif userInput == 'f' or userInput == 'F':
          GPIO.output(led_pin, False)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
