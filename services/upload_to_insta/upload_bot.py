from instabot import Bot
import os

class InstaBot:

    def __init__(self):
        pass

    def upload_image(self, path, caption):
        '''To upload the image on Instagram'''

        bot = Bot()
        bot.login(username=os.getenv('INSTAGRAM_USERNAME'), password=os.getenv('INSTAGRAM_PASSWORD'))
        bot.upload_photo(path, caption=caption)