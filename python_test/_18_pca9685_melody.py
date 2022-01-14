import smbus
import pca9685
import time

buzzer_pin = 11
melody = [262, 294, 330, 349, 392, 440, 494, 523]

i2c_bus = smbus.SMBus(1) # 1 : /dev/o2c-1 (port I2C1)
pwm = pca9685.PWM(i2c_bus)

pwm.setDuty(buzzer_pin, 2047)

try:
  for note in range(8):
    pwm.setFreq(melody[note])
    time.sleep(0.5)

except KeyboardInterrupt:
  pass

pwm.setDuty(buzzer_pin, 0)
i2c_bus.close()