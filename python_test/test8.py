# 문제 풀이9 
# 쓰레드

# 라즈베리파이 GPIO17 LED연결
# 라즈베리파이 GPIO27 LED연결
# 라즈베리파이 GPIO23 LED연결

# 1. 첫번째 LED는 0.5초 주기로 깜박
# 2. 두번째 LED는 1.5초 주기로 깜박
# 3. 세번째 LED는 2.5초 주기로 깜박

# 쓰레드 두개 이상 생성해서 로직 만들기
import RPi.GPIO as GPIO
import threading
import time

led_red_pin = 17
led_green_pin = 27
led_blue_pin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_red_pin, GPIO.OUT)
GPIO.setup(led_green_pin, GPIO.OUT)
GPIO.setup(led_blue_pin, GPIO.OUT)

GPIO.output(led_red_pin, False)
GPIO.output(led_green_pin, False)
GPIO.output(led_blue_pin, False)

flag_exit = False
def t1_main():
	while True:
		GPIO.output(led_green_pin, True)
		time.sleep(0.5)	
		GPIO.output(led_green_pin, False)
		time.sleep(0.5)
		if flag_exit: break

def t2_main():
	while True:
		GPIO.output(led_blue_pin, True)
		time.sleep(1.5)	
		GPIO.output(led_blue_pin, False)
		time.sleep(1.5)
		if flag_exit: break
		
t1 = threading.Thread(target=t1_main)
t1.start()
t2 = threading.Thread(target=t2_main)
t2.start()

try:
	while True:
		GPIO.output(led_red_pin, True)
		time.sleep(2.5)	
		GPIO.output(led_red_pin, False)
		time.sleep(2.5)	
		
except KeyboardInterrupt:
	pass
	
flag_exit = True
t1.join()
t2.join()	
GPIO.cleanup()
