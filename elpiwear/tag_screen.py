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

class tag_screen(screen.screen):

    def __init__(self):
        screen.screen.__init__(self)
        self.img.putdata([(0,0,255)]*(240*320))

        self.image = Image.open('me.png')
        self.image = self.image.rotate(90).resize((100,100))
        self.img.paste(self.image,(0,220,100,320))

        self.font = ImageFont.truetype('arial.ttf', 30)
        draw_rotated_text(self.img, 'Frederic Jacob', (0, 3), 90, ImageFont.truetype('arial.ttf', 33), fill=(255,0,0))
        draw_rotated_text(self.img, 'Software Engineer', (40, 30), 90, ImageFont.truetype('arial.ttf', 20), fill=(255,0,0))
        draw_rotated_text(self.img, 'C/C++, Python...', (110, 130), 90, ImageFont.truetype('arial.ttf', 25), fill=(255,0,0))
        draw_rotated_text(self.img, 'Linux kernel contributor', (140, 55), 90, ImageFont.truetype('arial.ttf', 25), fill=(255,0,0))
        draw_rotated_text(self.img, 'Tw: @IngenieurJacob', (170, 72), 90, ImageFont.truetype('arial.ttf', 25), fill=(255,0,0))
        draw_rotated_text(self.img, 'GH: fjacob21', (200, 167), 90, ImageFont.truetype('arial.ttf', 25), fill=(255,0,0))

    def update(self):
        pass
