# 문제 풀이4

# 라즈베리파이 보드의 GPIO 27번 핀으로 버튼 입력 받고
# GPIO 22번 핀으로 제어하는 LED 회로를 구성 하세요

# 버튼 입력은 외부 인터럽트 처리 or 반복문  사용하고 싶은거 사용

# 한번 누르면 LED 켜져있음.
# 한번 더 누르면 LED 꺼져있음.
# (Toggle 처리하기)
import RPi.GPIO as GPIO

button_pin = 27
led_pin = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

buttonInputPrev = False
ledOn = False

try:
  while True:
    buttonInput = GPIO.input(button_pin)

    if buttonInput and not buttonInputPrev:
      print("rising edge")
      ledOn = True if not ledOn else False
      GPIO.output(led_pin, ledOn)
    elif not buttonInput and buttonInputPrev:
      print("falling edge")
    else: pass

    buttonInputPrev = buttonInput
    
except KeyboardInterrupt:
  pass

GPIO.cleanup()

