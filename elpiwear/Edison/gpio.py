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
#
# Simple proxy class for access of the GPIO bus on the Raspberry Pi.
#

import mraa

IN = mraa.DIR_IN
OUT = mraa.DIR_OUT

class gpio:
    def __init__(self, pin, direction):
        self.gpio = mraa.Gpio(pin)
        self.gpio.dir(direction)

    def input(self):
        return self.gpio.read()

    def output(self, value):
        self.gpio.write(value)

    def on(self):
        self.gpio.write(1)

    def off(self):
        self.gpio.write(0)
