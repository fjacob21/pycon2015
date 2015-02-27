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


#Simple driver for the Adafruit ADS1015 board. Can be used in single shot
#conversion mode or in continuous mode

ADS1015_CONVERT_REG         = 0x0000
ADS1015_CONFIG_REG          = 0x0001
ADS1015_LOWTHRESH_REG       = 0x0002
ADS1015_HITHRESH_REG        = 0x0003

ADS1015_COMP_QUE_MASK       = 0x0003
ADS1015_COMP_QUE_1CONV      = 0x0000
ADS1015_COMP_QUE_2CONV      = 0x0001
ADS1015_COMP_QUE_4CONV      = 0x0002
ADS1015_COMP_QUE_DISABLED   = 0x0003

ADS1015_COMP_LAT_MASK       = 0x0004
ADS1015_COMP_LAT_DISABLE    = 0x0000
ADS1015_COMP_LAT_ENABLE     = 0x0004

ADS1015_COMP_POL_MASK       = 0x0008
ADS1015_COMP_POL_LOW        = 0x0000
ADS1015_COMP_POL_HIGH       = 0x0008

ADS1015_COMP_MODE_MASK      = 0x0010
ADS1015_COMP_MODE_TRAD      = 0x0000
ADS1015_COMP_MODE_WINDOW    = 0x0010

ADS1015_DR_MASK             = 0x00E0
ADS1015_DR_128SPS           = 0x0000
ADS1015_DR_250SPS           = 0x0020
ADS1015_DR_490SPS           = 0x0040
ADS1015_DR_920SPS           = 0x0060
ADS1015_DR_1600SPS          = 0x0080
ADS1015_DR_2400SPS          = 0x00A0
ADS1015_DR_3300SPS          = 0x00C0
ADS1015_DR_3300SPS          = 0x00E0

ADS1015_MODE_MASK           = 0x0100
ADS1015_MODE_CONTINUE       = 0x0000
ADS1015_MODE_SINGLE         = 0x0100

ADS1015_PGA_MASK            = 0x0E00
ADS1015_PGA_6_144V          = 0x0000
ADS1015_PGA_4_096V          = 0x0200
ADS1015_PGA_2_048V          = 0x0400
ADS1015_PGA_1_024V          = 0x0600
ADS1015_PGA_0_512V          = 0x0800
ADS1015_PGA_0_256V          = 0x0A00

ADS1015_MUX_MASK            = 0x7000
ADS1015_MUX_DIFF_0_1        = 0x0000
ADS1015_MUX_DIFF_0_3        = 0x1000
ADS1015_MUX_DIFF_1_3        = 0x2000
ADS1015_MUX_DIFF_2_3        = 0x3000
ADS1015_MUX_SINGLE_0        = 0x4000
ADS1015_MUX_SINGLE_1        = 0x5000
ADS1015_MUX_SINGLE_2        = 0x6000
ADS1015_MUX_SINGLE_3        = 0x7000

ADS1015_OS_MASK             = 0x8000
ADS1015_OS_BUSY             = 0x0000
ADS1015_OS_NOTBUSY          = 0x8000
ADS1015_OS_START            = 0x8000

ADS1015_DEF_LTRESH          = 0x8000
ADS1015_DEF_HTRESH          = 0x7FFF
ADS1015_RDY_LTRESH          = 0x0000
ADS1015_RDY_HTRESH          = 0x8FFF

class ads1015:

    def __init__(self,spi):
        self.spi = spi
        self.config = self.readconfig()
        self.channel = self.readchannel()

    def writeregister(self, register, value):
        self.spi.writeregister(register,value)

    def readregister(self, register):
        return self.spi.readregister(register)

    def readconfig(self):
        return self.readregister(ADS1015_CONFIG_REG);

    def writeconfig(self):
        self.writeregister(ADS1015_CONFIG_REG, self.config)

    def readlthresh(self):
        return self.readregister(ADS1015_LOWTHRESH_REG);

    def readhthresh(self):
        return self.readregister(ADS1015_HITHRESH_REG);

    def writelthresh(self, value):
        self.writeregister(ADS1015_LOWTHRESH_REG, value);

    def writehthresh(self, value):
        self.writeregister(ADS1015_HITHRESH_REG, value);

    def readresult(self):
        return self.readregister(ADS1015_CONVERT_REG)>>4

    def setcomparatorqueue(self,latch):
        if latch == 0:
            self.config = (self.config&(~ADS1015_COMP_QUE_MASK))|(ADS1015_COMP_QUE_DISABLED&ADS1015_COMP_QUE_MASK)
        elif latch == 1:
            self.config = (self.config&(~ADS1015_COMP_QUE_MASK))|(ADS1015_COMP_QUE_1CONV&ADS1015_COMP_QUE_MASK)
        elif latch == 2:
            self.config = (self.config&(~ADS1015_COMP_QUE_MASK))|(ADS1015_COMP_QUE_2CONV&ADS1015_COMP_QUE_MASK)
        elif latch == 4:
            self.config = (self.config&(~ADS1015_COMP_QUE_MASK))|(ADS1015_COMP_QUE_4CONV&ADS1015_COMP_QUE_MASK)

    def enablerdypin(self):
        self.setcomparatorqueue(1)
        self.writeconfig()
        self.writelthresh(ADS1015_RDY_LTRESH);
        self.writehthresh(ADS1015_RDY_HTRESH);

    def disablerdypin(self):
        self.setcomparatorqueue(0)
        self.writeconfig()
        self.writelthresh(ADS1015_DEF_LTRESH);
        self.writehthresh(ADS1015_DEF_HTRESH);

    def setchannel(self, channel, write=False):
        self.channel = channel
        if channel == 0:
            self.config = (self.config&(~ADS1015_MUX_MASK))|(ADS1015_MUX_SINGLE_0&ADS1015_MUX_MASK)
        elif channel == 1:
            self.config = (self.config&(~ADS1015_MUX_MASK))|(ADS1015_MUX_SINGLE_1&ADS1015_MUX_MASK)
        elif channel == 2:
            self.config = (self.config&(~ADS1015_MUX_MASK))|(ADS1015_MUX_SINGLE_2&ADS1015_MUX_MASK)
        elif channel == 3:
            self.config = (self.config&(~ADS1015_MUX_MASK))|(ADS1015_MUX_SINGLE_3&ADS1015_MUX_MASK)
        if write:
            self.writeconfig()

    def readchannel(self):
        channel = self.readconfig() & ADS1015_MUX_MASK
        if channel == ADS1015_MUX_SINGLE_0:
            return 0
        elif channel == ADS1015_MUX_SINGLE_1:
            return 1
        elif channel == ADS1015_MUX_SINGLE_2:
            return 2
        elif channel == ADS1015_MUX_SINGLE_3:
            return 3
        return -1

    def setstartbit(self, write=False):
        self.config = self.config | ADS1015_OS_START
        if write:
            self.writeconfig()

    def setcontinuemode(self):
        self.config = (self.config&(~ADS1015_MODE_MASK))|(ADS1015_MODE_CONTINUE&ADS1015_MODE_MASK)

    def setoneshotmode(self):
        self.config = (self.config&(~ADS1015_MODE_MASK))|(ADS1015_MODE_SINGLE&ADS1015_MODE_MASK)

    def setdatarate(self,rate):
        self.config = (self.config&(~ADS1015_DR_MASK))|(rate&ADS1015_DR_MASK)

    def start(self):
        self.setcontinuemode()
        self.writeconfig()

    def stop(self):
        self.setoneshotmode()
        self.writeconfig()

    def getvalue(self):
        self.setstartbit()
        count=0
        while(1):
            count=count+1
            if self.readconfig()&ADS1015_OS_MASK == ADS1015_OS_NOTBUSY:
                break
        return self.readresult()
