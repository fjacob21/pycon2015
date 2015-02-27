#Demo code for the Adafruit ADS1015 board using the Raspberry Pi
#The driver can also be used with the Ready pin using a GPIO to
#be used in an interrupt mode.

import Rpi.spi as SPI
import ads1015

DEVICE_ADDRESS = 0x48
SPI_PORT = 1

spi = SPI.spi(SPI_PORT,DEVICE_ADDRESS)
adc = ads1015.ads1015(spi)
adc.setchannel(0, True)

print "ADC value:" + hex(adc.getvalue())
