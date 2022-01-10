# 문제 풀이3

# GPIO 18번으로 제어하는 부저 회로 구성

# A 를 누르면 도를 0.5초 동안
# S 를 누르면 레를 0.5초 동안
# D 를 누르면 미를 0.5초 동안
# F 를 누르면 파를 0.5초 동안
# G 를 누르면 솔를 0.5초 동안
# H 를 누르면 라를 0.5초 동안
# J 를 누르면 시를 0.5초 동안
# K 를 누르면 도를 0.5초 동안

# melody = [262,294,330,349,392,440,494,523]

# 배열 활용, 반복문 활용

# PWM활용
# Pwm.ChangeDutyCycle()
# import RPi.GPIO as GPIO
# import time

# buzzer_pin = 18

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(buzzer_pin, GPIO.OUT)

# pwm = GPIO.PWM(buzzer_pin, 1.0)
# melody = [262,294,330,349,392,440,494,523]

# try:
#   while True:
#     userInput = input()
#     pwm.start(50.0)
#     if userInput == 'a' or userInput == 'A':
#       pwm.ChangeFrequency(melody[0])
#       time.sleep(0.5)
#     elif userInput == 's' or userInput == 'S':
#       pwm.ChangeFrequency(melody[1])
#       time.sleep(0.5)
#     elif userInput == 'd' or userInput == 'D':
#       pwm.ChangeFrequency(melody[2])
#       time.sleep(0.5)
#     elif userInput == 'f' or userInput == 'F':
#       pwm.ChangeFrequency(melody[3])
#       time.sleep(0.5)
#     elif userInput == 'g' or userInput == 'G':
#       pwm.ChangeFrequency(melody[4])
#       time.sleep(0.5)
#     elif userInput == 'h' or userInput == 'H':
#       pwm.ChangeFrequency(melody[5])
#       time.sleep(0.5)
#     elif userInput == 'j' or userInput == 'J':
#       pwm.ChangeFrequency(melody[6])
#       time.sleep(0.5)
#     elif userInput == 'k' or userInput == 'K':
#       pwm.ChangeFrequency(melody[7])
#       time.sleep(0.5)
#     pwm.stop()
# except KeyboardInterrupt:
#   pass

# GPIO.cleanup()
import RPi.GPIO as GPIO
import time

buzzer_pin =18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1.0)
pwm.start(0.0)
melody = [262,294,330,349,392,440,494,523] #melody
keys = ["a", "s", "d", "f", "g", "h", "j", "k"] #key

try:
	while True:		
		userInput = input() # for string
		print(userInput)
		for note in range(0,len(keys)):
			if userInput == keys[note]:
				pwm.ChangeFrequency(melody[note])
				pwm.ChangeDutyCycle(50.0)
				time.sleep(0.5)
				pwm.ChangeDutyCycle(0.0)
				break
except KeyboardInterrupt:
	pass
	
pwm.stop()
GPIO.cleanup()
