from PIL import Image
import requests, json, os

class TweekPik:
    tweetpik_uri = 'https://tweetpik.com/api/images'
    headers = {'Content-Type': 'application/json', 'authorization': os.getenv('TWEETPIK_AUTHORIZATION')}

    def __init__(self):
        '''Default constructor'''
        pass

    def fetch_tweet_image_url(self, tweet_id):
        '''To download get the url of the tweet image from tweetpik'''
        try:
            data = {
                "tweetId": tweet_id
            }

            response = requests.post(self.tweetpik_uri, headers = self.headers, data = json.dumps(data))

            if(response.status_code == 201):
                data = response.json()
                return data['url']
            else:
                print('Error occured in fetching the image!')
        except Exception as e:
            print(e)

    def download_image_using_tweet_id(self, tweet_id):
        '''To download the image using url'''

        image_url = self.fetch_tweet_image_url(tweet_id)

        res = requests.get(image_url, stream=True)
        if res.status_code == 200:
            path = 'downloads/' + image_url.split('/')[-1]
            with open(path, 'wb') as f:
                for chunk in res:
                    f.write(chunk)
            self.crop_image(path)
            return path
        else:
            print("Error Occured in downloading image!")

    def crop_image(self, path):
        '''To crop the image using PILLOW'''
        
        with Image.open(path) as im:

            width, height = im.size   # Get dimensions
            left = width/1000
            top = height/10
            right = width - width/1000
            bottom = height - height/1000

            # Here the image "im" is cropped and assigned to new variable im_crop
            im_crop = im.crop((left, top, right, bottom))

            im_crop.save(path, 'png')