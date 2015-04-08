import Image
import ImageDraw
import textwrap
import time

class screen:

    def __init__(self):
        self.img = Image.new("RGB",(240,320))
        self.back = Image.new('RGBA', (320, 240), (0,0,0,0))
        self.draw = ImageDraw.Draw(self.back)
        self.last_update = 0
        self.focus_time = 60*1;

    def update(self):
        self.img.paste(self.back.rotate(-90),(0,0,240,320))
        self.last_update = time.time()
        return True

    def draw_text(self, text, position, font, fill=(255,255,255)):
        self.draw.text(position, text, font=font, fill=fill)
        return self.draw.textsize(text, font=font)

    def draw_text_wrap(self, text, position, wrap, font, fill=(255,255,255)):
        lines = textwrap.wrap(text, width = wrap)
        y_text = position[1]
        max_width = 0
        for line in lines:
            width, height = font.getsize(line)
            self.draw_text(line,(position[0],y_text), font, fill)
            y_text += height
            if(width>max_width): max_width = width
        return  max_width,(y_text-position[1])

    def draw_image(self, image, position, mask=None):
        size = image.getbbox()
        size = image.size
        self.back.paste(image,(position[0], position[1], position[0] + size[0], position[1] + size[1]), mask)
        return size[0],size[1]
