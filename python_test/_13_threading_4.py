import threading
import time
import RPi.GPIO as GPIO

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(led_pin, 1000.0)
pwm.start(0)

flag_exit = False

def fading_led():
    while True:
        for t_high in range(0, 101):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.01)
        for t_high in range(100, -1, -1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.01)
            if flag_exit:
                break


tBL = threading.Thread(target=fading_led)
tBL.start()

try:
    while True:
        print("main")
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

flag_exit = True
tBL.join()

pwm.stop()
GPIO.cleanup()
