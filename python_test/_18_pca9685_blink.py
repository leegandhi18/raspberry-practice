import smbus
import pca9685
import time

led_pin = 11

i2c_bus = smbus.SMBus(1) # 1 : /dev/o2c-1 (port I2C1)
pwm = pca9685.PWM(i2c_bus)

pwm.setFreq(1000)

try:
  while True:
    pwm.setDuty(led_pin, 0)
    time.sleep(0.5)
    pwm.setDuty(led_pin, 4095)
    time.sleep(0.5)

except KeyboardInterrupt:
  pass

pwm.setDuty(led_pin, 0)
i2c_bus.close()