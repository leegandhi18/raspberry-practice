# 문제 풀이7  
# 사용자 입력 다중 출력

# 라즈베리파이 보드의 GPIO 17번 LED 연결
# 라즈베리파이 보드의 GPIO 18번 LED 연결

# 사용자가 확인 할 수 있도록 처음에 print로 menu를 만들고 아래 로직을 만들어 주세요.

# n입력은 첫번째 LED 켜기
# F입력은 첫번쨰 LED 끄기
# 0입력은 두번째 LED 밝기 0%
# 5입력은 두번째 LED 밝기 50%
# t입력은 두번째 LED 밝기 100%
import RPi.GPIO as GPIO
import time

led_red_pin = 17
led_blue_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_red_pin, GPIO.OUT)
GPIO.setup(led_blue_pin, GPIO.OUT)


GPIO.output(led_red_pin, False)

pwm_blue_led = GPIO.PWM(led_blue_pin, 1000.0)
pwm_blue_led.start(0.0) # 0.0~100.0

def showMenu():
	print("==<<MENU>>==");
	print("n. 빨간색 LED 켜기");
	print("f. 빨간색 LED 끄기");
	print("0. 파란색 LED 밝기 0%");
	print("5. 파란색 LED 밝기 50%");
	print("t. 파란색 LED 밝기 100%");
	
showMenu()

while True:
	userInput = input(">>>");
	print(userInput)
	if userInput == "n":
		GPIO.output(led_red_pin, True)
	elif userInput == "f":
		GPIO.output(led_red_pin, False)
	if userInput == "0":
		pwm_blue_led.ChangeDutyCycle(0)
	elif userInput == "5":
		pwm_blue_led.ChangeDutyCycle(50)
	elif userInput == "t":
		pwm_blue_led.ChangeDutyCycle(100)

pwm.stop()
GPIO.cleanup()