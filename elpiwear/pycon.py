import time
import Rpi.i2c as I2C
import Rpi.gpio as GPIO
import Rpi.spi as SPI
import screen
import ILI9341 as TFT
import watchout_screen
import twitter_screen
import tag_screen
import gplus_screen
import time

class pycon():

    def __init__(self):
        print 'Super secret Pycon tag screen'
        self.init_display()
        self.init_screens()
        detect = GPIO.gpio(18, GPIO.IN)
        while 1:
            self.screens[self.current_screen].update()
            self.disp.display(self.screens[self.current_screen].img)
            screen_start = time.time()
            while (time.time()-screen_start) < self.screens[self.current_screen].focus_time:
                if self.screens[self.current_screen].update():
                    self.disp.display(self.screens[self.current_screen].img)
                time.sleep(0.100)
                if detect.input() == 1 and (time.time()-self.watchout.last_update) > 60*5:
                    self.current_screen = 3
            self.current_screen = (self.current_screen + 1) % (len(self.screens)-1) #To remove watchout screen

    def init_display(self):
        dc = GPIO.gpio(4, GPIO.OUT)
        rst = GPIO.gpio(17, GPIO.OUT)
        self.disp = TFT.ILI9341(dc, rst=rst, spi=SPI.spi(0, 0))
        self.disp.begin()

    def init_screens(self):
        self.tag = tag_screen.tag_screen()
        self.watchout = watchout_screen.watchout_screen()
        self.twitter = twitter_screen.twitter_screen()
        self.gplus = gplus_screen.gplus_screen()
        self.screens = [self.tag, self.twitter, self.gplus, self.watchout]
        self.current_screen = 0

if __name__ == "__main__":
    main = pycon()
