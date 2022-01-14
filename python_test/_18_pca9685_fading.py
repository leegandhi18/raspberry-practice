import smbus
import pca9685
import time

led_pin = 11

i2c_bus = smbus.SMBus(1) # 1 : /dev/o2c-1 (port I2C1)
pwm = pca9685.PWM(i2c_bus)

pwm.setFreq(1000)

try:
  while True:
    for dutyCycle in range(0, 4096, 8):
      pwm.setDuty(led_pin, dutyCycle)
      time.sleep(0.001)
    for dutyCycle in range(4095, -1, -8):
      pwm.setDuty(led_pin, dutyCycle)
      time.sleep(0.001)

except KeyboardInterrupt:
  pass

pwm.setDuty(led_pin, 0)
i2c_bus.close()