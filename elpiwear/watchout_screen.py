import Image
import ImageDraw
import ImageFont
import screen

def draw_rotated_text(image, text, position, angle, font, fill=(255,255,255)):
    # Get rendered font width and height.
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    # Create a new image with transparent background to store the text.
    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    # Render the text.
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    # Rotate the text image.
    rotated = textimage.rotate(angle, expand=1)
    # Paste the text into the image, using it as a mask for transparency.
    image.paste(rotated, position, rotated)

class watchout_screen(screen.screen):

    def __init__(self):
        screen.screen.__init__(self)
        self.image = Image.open('maximus.jpg')
        self.image = self.image.rotate(90).resize((240,320))
        self.img.paste(self.image)
        #font = ImageFont.load_default()
        self.bfont = ImageFont.truetype('arial.ttf', 66)
        self.font = ImageFont.truetype('arial.ttf', 65)
        self.count = 0
        draw_rotated_text(self.img, 'Watchout!!', (130, -3), 90, self.bfont, fill=(255,0,0))
        draw_rotated_text(self.img, 'Watchout!!', (130, 0), 90, self.font, fill=(255,255,255))

    def update(self):
        self.img.paste(self.image)
        if self.count == 0 :
            draw_rotated_text(self.img, 'Watchout!!', (130, -3), 90, self.bfont, fill=(255,255,255))
            draw_rotated_text(self.img, 'Watchout!!', (130, 3), 90, self.font, fill=(255,0,0))

        else:
            draw_rotated_text(self.img, 'Watchout!!', (130, -3), 90, self.bfont, fill=(255,0,0))
            draw_rotated_text(self.img, 'Watchout!!', (130, 0), 90, self.font, fill=(255,255,255))
        self.count = 1 - self.count
