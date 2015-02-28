import smbus

class i2c:
    def __init__(self, i2cport, i2caddress):
        self.address = i2caddress
        self.bus = smbus.SMBus(i2cport)

    def writeregister(self, register, value):
        value = ((value&0xff) << 8) | (value>>8)
        self.bus.write_word_data(self.address, register, value)

    def readregister(self, register):
        value = self.bus.read_word_data(self.address, register)
        value = ((value&0xff) << 8) | (value>>8)
        return value
