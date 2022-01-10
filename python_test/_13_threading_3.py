import threading
import time
import RPi.GPIO as GPIO

led_pin = 17

flag_exit = False
def blink_led():
  while True:
    GPIO.output(led_pin, True)
    time.sleep(0.5)
    GPIO.output(led_pin, False)
    time.sleep(0.5)

    if flag_exit: break

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

tBL = threading.Thread(target=blink_led)
tBL.start()

try:
  while True:
    print("main")
    time.sleep(1.0);

except KeyboardInterrupt:
  pass

flag_exit = True
tBL.join()