import Image
import ImageDraw

class screen:

    def __init__(self):
        self.img = Image.new("RGB",(240,320))
        self.draw = ImageDraw.Draw(self.img)

    def update(self):
        pass
