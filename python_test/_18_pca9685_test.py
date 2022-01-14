# I2C 버스 응용하기
# A누르면 LED 밝기 최대
# S누르면 LED 꺼짐
# D누르면 LED 점멸
import smbus
import pca9685
import time
import threading
led_pin =11

i2c_bus = smbus.SMBus(1)
pwm = pca9685.PWM(i2c_bus)

pwm.setFreq(1000)

flag_exit = False
userInput ="f"
def blink_led():
  global userInput
  while True:
    if userInput == "a":
      pwm.setDuty(led_pin, 4095)
    elif userInput == "s":
      pwm.setDuty(led_pin, 0)
    elif userInput == "d":
      pwm.setDuty(led_pin, 4095)
      time.sleep(0.5)
      pwm.setDuty(led_pin, 0)
      time.sleep(0.5)
    else:
      pwm.setDuty(led_pin, 0)

    if flag_exit: break
    
tBL = threading.Thread(target=blink_led)
tBL.start()

try:
  while True:
    userInput = input() # for string
    print(userInput)

except KeyboardInterrupt:
  pass

tBL.join()
pwm.setDuty(led_pin,0)
i2c_bus.close()