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


#Simple driver for the Sharp 2Y0A21 analog distance sensor.
#Need to receive the calibration fron a json file with the folowing
#format [{"distance"}:distance,"value":adcvalue]
#
#There is also a simple script for the Raspberry Pi to build the calibaration:
#dist_sensor_calib.py
#This driver calculate the distance using a linear interpolation of the
#calibration data. This is not always acurate but good enough if used
#between 10cm to 80cm.

import json

class sharp2y0a21:
    def __init__(self, adc=None):
        self.init = 0
        self.adc = adc
        self.samples = []

    def calculate(self, value):
        last = None
        for sample in self.samples:
            if value > sample['value']:
                if last is None:
                    return sample['distance']

                lastd = float(last['distance'])
                lastv = float(last['value'])
                sampd = float(sample['distance'])
                sampv = float(sample['value'])
                distance = lastd + ((sampd - lastd) *((value-lastv)/(sampv-lastv)) )
                return distance
            last = sample
        return 0

    def distance(self):
        return self.calculate(self.adc.getvalue())

    def loadcalibration(self, filename):
        with open(filename,'r') as file:
            samples = json.load(file)
            self.samples = sorted(samples, key=lambda k: k['distance'])
