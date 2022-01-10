# 문제 풀이5

# 라즈베리파이 보드의 GPIO 27번 핀으로 버튼 입력 받고
# GPIO 22번 핀으로 제어하는 LED 회로를 구성 하세요

# 버튼 입력은 외부 인터럽트 처리 or 반복문  사용하고 싶은거 사용

# 한번 누르면 LED 밝기 0%.
# 한번 더 누르면 LED 밝기 50%.
# 한번 더 누르면 LED 밝기 100%
# 한번 더 누르면 LED 밝기 0% … 1,2,3 반복

# 조건문으로 상태 변경 처리
import RPi.GPIO as GPIO
import time

button_pin = 27
led_pin = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 1000.0)
pwm.start(0.0) # 0.0 ~ 100.0

buttonInputPrev = False
cnt = 0

try:
  while True:
    buttonInput = GPIO.input(button_pin)
    if buttonInput and not buttonInputPrev:
      cnt = cnt + 1
      if cnt == 3:
        cnt = 0
      print(cnt)
      time.sleep(0.3) # delay
      if cnt == 0:
        pwm.ChangeDutyCycle(0)
      elif cnt == 1:
        pwm.ChangeDutyCycle(50)
      elif cnt == 2:
        pwm.ChangeDutyCycle(100)

    buttonInputPrev = buttonInput
    
except KeyboardInterrupt:
  pass

GPIO.cleanup()


