import Image
import ImageDraw
import ImageFont
import screen
import time

class tag_screen(screen.screen):

    def __init__(self):
        screen.screen.__init__(self)
        self.me = Image.open('me.png')
        self.me = self.me.resize((100,100))
        self.display_tag()
        self.update()

    def display_tag(self):
        self.back.putdata([(255,255,255)]*(240*320))
        lw,lh = self.draw_image(self.me, (0,0))
        self.draw_text('Frederic Jacob', (lw + 3, 0), ImageFont.truetype('Montserrat-Bold.ttf', 28), fill=(0,0,0))
        self.draw_text('Software Engineer', (lw + 3, 30), ImageFont.truetype('Montserrat-Regular.ttf', 23), fill=(0,0,0))
        self.draw_text(time.strftime('%H:%M'), (lw + 70, 70), ImageFont.truetype('Montserrat-Regular.ttf', 23), fill=(0,0,0))
        self.draw_text('C/C++, Python...', (5, lh+10), ImageFont.truetype('Montserrat-Regular.ttf', 25), fill=(0,0,0))
        self.draw_text('Linux kernel contributor', (5, lh + 40), ImageFont.truetype('Montserrat-Regular.ttf', 25), fill=(0,0,0))
        twimg = Image.open("Twitter_logo_blue.png").resize((20,20))
        tw,th = self.draw_image(twimg, (5,lh + 78), twimg)
        self.draw_text(': @IngenieurJacob', (tw+10, lh + 70), ImageFont.truetype('Montserrat-Regular.ttf', 25), fill=(0,0,0))
        ghimg = Image.open("GitHub-Mark-32px.png").resize((20,20))
        gw,gh = self.draw_image(ghimg, (5,lh + 108), ghimg)
        self.draw_text(': fjacob21', (gw + 10, lh + 100), ImageFont.truetype('Montserrat-Regular.ttf', 25), fill=(0,0,0))

    def update(self):
        self.display_tag()
        return screen.screen.update(self)
