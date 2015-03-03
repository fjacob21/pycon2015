import mraa

class i2c:
    def __init__(self, i2cport, i2caddress):
        self.bus = mraa.I2c(i2cport)
        self.bus.address(i2caddress)

    def writeregister(self, register, value):
        value = ((value&0xff) << 8) | (value>>8)
        self.bus.writeWordReg(register, value)

    def readregister(self, register):
        value = self.bus.readWordReg(register)
        value = ((value&0xff) << 8) | (value>>8)
        return value
