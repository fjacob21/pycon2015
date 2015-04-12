import Image
import ImageDraw
import ImageFont
import screen
import twitter
import urllib
import textwrap
import re
import time
from HTMLParser import HTMLParser

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
        self.twitter = twitter.Twitter(auth=twitter.OAuth(self.token, self.token_key, self.con_secret, self.con_secret_key))
        self.twimage = Image.open(self.param["logo"])
        self.twimage = self.twimage.resize((40,40))
        self.update_time = 60*15 #In second!!
        self.display_last_tweet()

    def update(self):
        if (time.time() - self.last_update) > self.update_time:
            return self.display_last_tweet()
        return False

    def display_last_tweet(self):
        pycon = self.get_latess_tweet()
        if pycon is not None:
            self.back.putdata([self.param["backcolor"]]*(240*320))
            ax,ay = self.display_avatar(pycon, (5,5))
            ux,uy = self.display_user(pycon, (ax+10, 5))
            self.draw_image(self.twimage,(ax+10+ux+10,5),self.twimage)
            self.display_text(pycon, (0, ay+10))
            self.last_pycon = pycon
            return screen.screen.update(self)
        return False

    def get_latess_tweet(self):
        try:
            pycon = self.twitter.search.tweets(q="#pycon+pycon+#PyCon2015", lang="en")
            user = pycon["statuses"][0]["user"]["screen_name"].encode('utf-8')
            name = pycon["statuses"][0]["user"]["name"].encode('utf-8')
            text = pycon["statuses"][0]["text"] #.encode('utf-8')
            text = HTMLParser().unescape(text)
            #text = re.sub(r'^http?:\/\/.*[\r\n]*', '', text)
            text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
            avatar = pycon["statuses"][0]["user"]["profile_image_url"].encode('utf-8')
            avatar_filename = "avatar.img" #avatar.split('/')[-1]
            urllib.urlretrieve (avatar, avatar_filename)
            return {"user":user,"name":name,"text":text,"avatar":avatar_filename}
        except:
            return None

    def display_avatar(self,pycon, position):
        self.image = Image.open(pycon["avatar"])
        self.image = self.image.resize((55,55))
        return self.draw_image(self.image, position)

    def display_user(self,pycon, position):
        nw,nh = self.draw_text(pycon["name"], position, ImageFont.truetype('Montserrat-Bold.ttf', 20), fill=self.param["textcolor"])
        uw,uh = self.draw_text('@' + pycon["user"], (position[0], position[1]+nh+5), ImageFont.truetype('Montserrat-Regular.ttf', 20), fill=self.param["textcolor"])
        return max(nw,uw),nh+uh+5

    def display_text(self, pycon,position):
        self.draw_text_wrap(pycon["text"], position, 25, ImageFont.truetype('Montserrat-Regular.ttf', 22), fill=self.param["textcolor"])
