import Image
import ImageDraw
import ImageFont
import screen
import twitter
import urllib
import textwrap

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
    return width, height

class twitter_screen(screen.screen):

    def __init__(self):
        screen.screen.__init__(self)
        self.params = {"white":{"backcolor":(255,255,255),"textcolor":(0,0,0), "logo":"Twitter_logo_blue.png"},
                        "blue":{"backcolor":(85,112,238),"textcolor":(0,0,0), "logo":"Twitter_logo_white.png"}}
        self.param = self.params["white"]
        self.token = "45400388-ecZ5cD6IAA2J1fOzPXbzVSmCVHUt6sQ5HePRqE7zP"
        self.token_key = "lkXmLQ3WvaOEuL7C0DhMedn3vL18xiSXNEGy3grIj267x"
        self.con_secret = "Mw1OHJoR7MEKBb4JyfW7twMbP"
        self.con_secret_key = "jsSWH9w5xF7102MTEvoYixECFzIh4ZeaPp9H30baSxW2UISl4R"
        self.back = Image.new('RGBA', (320, 240), (0,0,0,0))
        self.twitter = twitter.Twitter(auth=twitter.OAuth(self.token, self.token_key, self.con_secret, self.con_secret_key))
        self.twimage = Image.open(self.param["logo"])
        self.twimage = self.twimage.resize((40,40))
        self.display_last_tweet()

    def update(self):
        self.display_last_tweet()

    def display_last_tweet(self):
        pycon = self.get_latess_tweet()
        self.back.putdata([self.param["backcolor"]]*(240*320))

        ax,ay = self.display_avatar(pycon)
        ux,uy = self.display_user(pycon, ax+5)
        self.back.paste(self.twimage,(ux+30,5,ux+30+40,45),self.twimage)
        self.display_text(pycon, 0, ay+5)
        self.img.paste(self.back.rotate(-90),(0,0,240,320))

    def get_latess_tweet(self):
        # Get your "home" timeline
        pycon = self.twitter.search.tweets(q="pycon", lang="en")
        user = pycon["statuses"][0]["user"]["screen_name"].encode('utf-8')
        name = pycon["statuses"][0]["user"]["name"].encode('utf-8')
        text = pycon["statuses"][0]["text"].encode('utf-8')
        avatar = pycon["statuses"][0]["user"]["profile_image_url"].encode('utf-8')
        avatar_filename = avatar.split('/')[-1]
        urllib.urlretrieve (avatar, avatar_filename)
        return {"user":user,"name":name,"text":text,"avatar":avatar_filename}

    def display_avatar(self,pycon):
        self.image = Image.open(pycon["avatar"])
        self.image = self.image.resize((55,55))
        self.back.paste(self.image,(5,5,60,60))
        return 60,60

    def display_user(self,pycon,x=60,y=0):
        nw,nh = draw_rotated_text(self.back, pycon["name"], (x, y), 0, ImageFont.truetype('Montserrat-Bold.ttf', 20), fill=self.param["textcolor"])
        uw,uh = draw_rotated_text(self.back, '@' + pycon["user"], (x, y+25), 0, ImageFont.truetype('Montserrat-Regular.ttf', 20), fill=self.param["textcolor"])
        return x+max(nw,uw),y+25+uh

    def display_text(self, pycon,x=0,y=60):
        self.draw_text_wrap(pycon["text"], 25, ImageFont.truetype('Montserrat-Regular.ttf', 22), self.back, x, y)

    def draw_text_wrap(self, text, wrap, font, img, x=0, y=60):
        lines = textwrap.wrap(text, width = wrap)
        y_text = y
        for line in lines:
            width, height = font.getsize(line)
            draw_rotated_text(img, line, (x, y_text), 0,font, fill=self.param["textcolor"])
            y_text += height
