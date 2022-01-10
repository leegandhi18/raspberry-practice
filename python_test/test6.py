# 문제 풀이6

# 라즈베리파이 보드의 GPIO 22번 핀으로 버튼 입력 받고
# GPIO 18번 핀으로 부저 회로 구성

# 버튼 입력은 외부 인터럽트 처리 or 반복문  사용하고 싶은거 사용

# 누를때마다 도,레,미,파,솔,라,시,도 소리 변경되게 작성

# 조건문으로 상태 변경 처리
import RPi.GPIO as GPIO
import time

button_pin = 22
buzzer_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1.0)
pwm.start(0.0)

melody = [262,294,330,349,392,440,494,523]

buttonInputPrev = False
cnt = 0

try:
	while True:
		buttonInput = GPIO.input(button_pin)
		# print(buttonInput)
				
		if buttonInput and not buttonInputPrev:
			cnt = cnt + 1
			if cnt == 8: 
				cnt = 0
			print(cnt);
		
			pwm.ChangeFrequency(melody[cnt])
			pwm.ChangeDutyCycle(50.0)
			time.sleep(0.5)
			pwm.ChangeDutyCycle(0.0)
		
		buttonInputPrev = buttonInput
			
except KeyboardInterrupt:
	pass
	
pwm.stop()
GPIO.cleanup()