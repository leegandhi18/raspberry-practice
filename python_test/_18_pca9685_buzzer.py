import smbus
import pca9685
import time

buzzer_pin = 11

i2c_bus = smbus.SMBus(1) # 1 : /dev/o2c-1 (port I2C1)
pwm = pca9685.PWM(i2c_bus)

pwm.setDuty(buzzer_pin, 2047)

try:
  for cnt in range(3):
    pwm.setFreq(262)
    time.sleep(1.0)
    pwm.setFreq(294)
    time.sleep(1.0)

except KeyboardInterrupt:
  pass

pwm.setDuty(buzzer_pin, 0)
i2c_bus.close()