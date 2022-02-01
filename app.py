from flask import Flask, jsonify, render_template, request
from apscheduler.schedulers.background import BackgroundScheduler

from services.coinswitch.coinswitch import Coinswitch
from services.mailer.mailer import Mail
from services.tweet_to_image.tweetpik import TweekPik
from services.upload_to_insta.upload_bot import InstaBot
from services.db.db import DB

import os

from dotenv import load_dotenv

env_path = '/home/powerfist01/hawk-eyed/.env'
load_dotenv(env_path)  # take environment variables from .env

app = Flask(__name__)

@app.route('/')
def main():
    return 'Server is running hot!!!'

@app.route('/coinswitch')
def coinswitch():
    coinswitch = Coinswitch()
    coins = coinswitch.get_latest_data()
    return render_template('index.html', coins = coins)

@app.route('/get_total_info/<coin>')
def total_info(coin):

    coinswitch = Coinswitch()
    coin_data = coinswitch.get_latest_data(coin)
    return coin_data

@app.route('/instagram', methods =['GET', 'POST'])
def instagram():

    if(request.method == 'POST'):
        tweet_id = request.json['tweet_id']
        tags = request.json['tags']
        tweetPik = TweekPik()
        path = tweetPik.download_image_using_tweet_id(tweet_id)

        insta_bot = InstaBot()
        insta_bot.upload_image(path, tags)

        return {'success': True, 'data': tweet_id}
    else:
        return render_template('instagram.html')

@app.route('/testing')
def testing():

    return {'data': 'testing'}

if __name__ == '__main__':
    app.run(debug=True)
