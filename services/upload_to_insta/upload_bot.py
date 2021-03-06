from instabot import Bot
import os, shutil, time
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

class InstaBot:

    def __init__(self):
        pass

    def upload_image(self, path, caption):
        '''To upload the image on Instagram'''
        try:
            time.sleep(5)
            bot = Bot()
            time.sleep(5)
            bot.login(username=os.environ['INSTAGRAM_USERNAME'], password=os.environ['INSTAGRAM_PASSWORD'], is_threaded=True)
            time.sleep(5)
            bot.upload_photo(path, caption=caption)
            time.sleep(5)
            self.remove_files()
            self.remove_config_folder()
        except Exception as e:
            print('Error occured!', e)

    def remove_files(self):
        
        folder = 'downloads'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    if(not file_path.endswith('needed')):
                        os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def remove_config_folder(self):
        
        try:
            folder = 'config'
            shutil.rmtree(folder)
        except Exception as e:
            print('Error occured!')