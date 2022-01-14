import time

MODE1 =0x00
PRE_SCALE =0xFE
LED0_OFF_L =0x08
LED0_OFF_H =0x09

SLEEP =0x10
RESTART =0x80

class PWM:
	def __init__(self, bus, address =0x40):
		self.bus = bus
		self.address = address
		self._writeByte(MODE1, 0x00)
	
	def setFreq(self, frequency):
		baseMode = self._readByte(MODE1)&0xFF
		self._writeByte(MODE1, baseMode|SLEEP)
		
		prescale = (25000000.0/(4096*frequency)+0.5)-1
		self._writeByte(PRE_SCALE, int(prescale))
		
		self._writeByte(MODE1, baseMode)
		
		time.sleep(0.001)
		
		self._writeByte(MODE1, baseMode|RESTART)
	
	def setDuty(self, pin, duty_cycle):
		chan = pin*4
		duty_off =int(duty_cycle)&0xFFFF
		self._writeByte(LED0_OFF_L+chan, duty_off&0xFF)
		self._writeByte(LED0_OFF_H+chan, duty_off>>8)

	def _writeByte(self, reg, value):
		try:
			self.bus.write_byte_data(self.address, reg, value)
		except:
			print ("Error while writing to I2C device")
			
	def _readByte(self, reg):
		try:
			value = self.bus.read_byte_data(self.address, reg)
			return value
		except:
			print ("Error while reading from I2C device")
			return None