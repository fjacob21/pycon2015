#Demo code for the Adafruit ADS1015 board using the Raspberry Pi
#and the Intel Edison.
#The driver can also be used with the Ready pin using a GPIO to
#be used in an interrupt mode.

#import Rpi.i2c as I2C
import Edison.i2c as I2C
import ads1015

DEVICE_ADDRESS = 0x48
I2C_PORT = 1

i2c = I2C.i2c(I2C_PORT,DEVICE_ADDRESS)
adc = ads1015.ads1015(i2c)
adc.setchannel(0, True)

print "ADC value:" + hex(adc.getvalue())
