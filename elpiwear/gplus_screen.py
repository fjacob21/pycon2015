import Image
import ImageDraw
import ImageFont
import screen
import urllib2
import urllib
import textwrap
import json
import re
import time
from HTMLParser import HTMLParser

class gplus_screen(screen.screen):

    def __init__(self):
        screen.screen.__init__(self)
        self.params = {"white":{"backcolor":(255,255,255),"textcolor":(0,0,0), "logo":"Red-signin-Small-base-44dp.png"},
                        "red":{"backcolor":(85,112,238),"textcolor":(0,0,0), "logo":"Red-signin-Small-base-44dp.png"}}
        self.param = self.params["white"]
        self.posturl = "https://www.googleapis.com/plus/v1/activities?query=pycon%2C%23pycon%2CPyCon2015%2C%23PyCon2015&language=en&key=AIzaSyDDNE6OhN1PxPNRwYxlct6ZXj1VX67Pxo8"
        self.twimage = Image.open(self.param["logo"])
        self.twimage = self.twimage.resize((40,40))
        self.update_time = 60*15 #In second!!
        self.display_last_post()

    def update(self):
        if (time.time() - self.last_update) > self.update_time:
            return self.display_last_post()
        return False

    def display_last_post(self):
        pycon = self.get_latess_post()
        if pycon is not None:
            self.back.putdata([self.param["backcolor"]]*(240*320))
            ax,ay = self.display_avatar(pycon, (5,5))
            ux,uy = self.display_user(pycon, (ax+10, 5))
            self.draw_image(self.twimage,(ax+10+ux+10,5),self.twimage)
            self.display_text(pycon, (0, ay+10))
            self.last_pycon = pycon
            return screen.screen.update(self)
        return False

    def get_latess_post(self):
        try:
            response = urllib2.urlopen(self.posturl)
            posts = response.read()
            pycon = json.loads(posts)
            user = pycon["items"][0]["actor"]["displayName"].encode('utf-8')
            text = pycon["items"][0]["object"]["content"] #.encode('utf-8')
            text = HTMLParser().unescape(text)
            tag=re.compile(r'<[^>]+>')
            text = tag.sub('',text)
            text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
            #text = re.sub(r'^http?:\/\/.*[\r\n]*', '', text)
            self.text=text
            self.textu = pycon["items"][0]["object"]["content"]
            avatar = pycon["items"][0]["actor"]["image"]["url"].encode('utf-8')
            avatar_filename = 'photo.jpg'
            urllib.urlretrieve (avatar, avatar_filename)
            return {"user":user,"text":text,"avatar":avatar_filename}
        except:
            return None

    def display_avatar(self,pycon, position):
        self.image = Image.open(pycon["avatar"])
        self.image = self.image.resize((55,55))
        return self.draw_image(self.image, position)

    def display_user(self,pycon, position):
        nw,nh = self.draw_text_wrap(pycon["user"], position, 10, ImageFont.truetype('Montserrat-Bold.ttf', 18), fill=self.param["textcolor"])
        return nw,nh

    def display_text(self, pycon,position):
        self.draw_text_wrap(pycon["text"], position, 25, ImageFont.truetype('Montserrat-Regular.ttf', 22), fill=self.param["textcolor"])
