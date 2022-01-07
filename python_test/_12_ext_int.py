# import RPi.GPIO as GPIO

# led_state = False
# led_state_changed = False
# def buttonPressed(channel):
#   global led_state
#   global led_state_changed
#   led_state = True if not led_state else False
#   led_state_changed = True

# button_pin = 27
# led_pin = 22

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(led_pin, GPIO.OUT)

# GPIO.setup(button_pin, GPIO.IN)
# GPIO.add_event_detect(button_pin, GPIO.RISING)
# GPIO.add_event_callback(button_pin, buttonPressed)

# try:
#   while True:
#     if led_state_changed == True:
#       led_state_changed = False
#       GPIO.output(led_pin, led_state)

# except KeyboardInterrupt:
#   pass

# GPIO.cleanup()

import RPi.GPIO as GPIO

led_state = False
led_state_changed = False
def buttonPressed(channel):   # 이벤트 발생시 처리 함수 
	global led_state            # led_state 전역 변수 선언
	global led_state_changed    # led_state_changed 전역 번수 선언
	led_state = True if not led_state else False  #led state가 true면 false로 바꾸고, False상태면 True로 변경함
	led_state_changed = True    #함수 처리 후 led_state_chaged 변수 True로 처리

button_pin =27
led_pin =22

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

GPIO.setup(button_pin, GPIO.IN)
GPIO.add_event_detect(button_pin, GPIO.RISING)  # event감지하는 방법 GPIO 핀이 low에서 High로 올라 갈떄 감지
GPIO.add_event_callback(button_pin, buttonPressed) # event 감지 후 불러올 함수 선언 Callback

try:
	while True:
		if led_state_changed == True:       #led_state_change가 True면 False로 다시 돌려 놓음
			led_state_changed = False
			GPIO.output(led_pin, led_state)
	
except KeyboardInterrupt:
	pass
	
GPIO.cleanup()


