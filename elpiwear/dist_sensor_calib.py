# The MIT License (MIT)
#
# Copyright (c) 2015 Frederic Jacob
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#Simple calibration script for the Sharp 2Y0A21 analog distance sensor.
#Will generate a json file that is a good calibration file to load with the
#sharp2Y0A21.py mini driver loadcalibration function.
#Work with the Raspberry Pi so far using the external i2c wrapper Rpi/i2c.py

import json
import Rpi.i2c as I2C
import ads1015

class calibrator:

    def __init__(self):
        self.adc = ads1015.ads1015(I2C.i2c(1,0x48))
        self.adc.setchannel(0, True)
        self.adc.setdatarate(ads1015.ADS1015_DR_128SPS)
        self.samples = []

    def execute(self):
        print 'Welcome to the linear distance sensor calibration software!\n'
        print 'To calibrate the sensor position an object to a know distance and enter it.\n'
        print 'I will get a sample from the ADC and I will associate the entered distance\n'
        print 'with the sensor value. \n'
        print 'Enter q to terminate\nand please be kind with the distance string, I am easyly disturbed ;)\n'

        end = False
        while(not end):
            diststr = raw_input('Distance: ')
            if diststr == 'q':
                end = True
            else:
                dist = float(diststr)
                self.addsample(self.adc.getvalue(), dist)

        print 'Thanks you for your calibration samples, here the results table\n'
        self.savecalibration()

    def addsample(self, value, distance):
        self.samples.append({"value":value, "distance":distance})

    def savecalibration(self):
        print 'Here is the samples from the calibration:\n'
        print json.dumps(self.samples)
        if raw_input('Do you want to save it?') in ['Y', 'y', 'Yes', 'yes', 'YES']:
            filename = raw_input('What name do you want this calibration to be remember?')
            with open(filename,'w') as file:
                json.dump(self.samples, file)

if __name__ == "__main__":
    calib = calibrator()
    calib.execute()
