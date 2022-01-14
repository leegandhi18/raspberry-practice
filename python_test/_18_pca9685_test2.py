# I2C 버스 응용하기
# 입력받은 freq 값 대로 소리내기
# 262 입력하면 262 해당되는 소리
# 294 입력하면 294 해당되는 소리
# 525 입력하면 525 해당되는 소리
import smbus
import pca9685
import time

buzzer_pin = 11
# melody = [262, 294, 330, 349, 392, 440, 494, 523]


i2c_bus = smbus.SMBus(1)
pwm = pca9685.PWM(i2c_bus)

pwm.setDuty(buzzer_pin, 0)

try:
  while True:
    userInput = input()
    pwm.setFreq(int(userInput))
    pwm.setDuty(buzzer_pin, 2047)
    time.sleep(2.0)
    pwm.setDuty(buzzer_pin, 0)



except KeyboardInterrupt:
  pass

pwm.setDuty(buzzer_pin, 0)
i2c_bus.close()