import Image
import ImageDraw
import ImageFont
import screen

class watchout_screen(screen.screen):

    def __init__(self):
        screen.screen.__init__(self)
        self.image = Image.open('maximus.jpg')
        self.image = self.image.resize((320,240))
        self.draw_image(self.image , (0,0))

        self.bfont = ImageFont.truetype('Montserrat-Regular.ttf', 66)
        self.font = ImageFont.truetype('Montserrat-Regular.ttf', 65)
        self.count = 0
        self.display()

    def display(self):
        self.draw_image(self.image , (0,0))
        if self.count == 0 :
            self.draw_text('Watchout!!', (0, 100), self.bfont, fill=(255,255,255))
            self.draw_text('Watchout!!', (0, 100), self.font, fill=(255,0,0))
        else:
            self.draw_text('Watchout!!', (0, 100), self.bfont, fill=(255,0,0))
            self.draw_text('Watchout!!', (0, 100), self.font, fill=(255,255,255))
        self.count = 1 - self.count
        screen.screen.update(self)

    def update(self):
        self.display()
