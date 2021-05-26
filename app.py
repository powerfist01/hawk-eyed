from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from services.mailer.mailer import mail

import requests
import json

app = Flask(__name__)

coins_id = [1, 6, 220, 210, 276, 205]

coins = [
    {"id": 220, "name": "Aave", "rate": 28000}, 
    {"id": 210, "name": "Cardano", "rate": 140}, 
    {"id": 1, "name": "Bitcoin", "rate": 2900000}, 
    {"id": 6, "name": "Ethereum", "rate": 200000}, 
    {"id": 276, "name": "Polygon", "rate": 150}, 
    {"id": 205, "name": "Maker", "rate": 270000}
]

best_rate = {
    1: 2900000,
    6: 200000,
    205: 270000,
    210: 140,
    220: 28000,
    276: 150
}

def get_latest_data():

    resp = requests.get('https://coinswitch.co/proxy/in/api/v1/coins')
    if(resp.status_code == 200):
        data = []
        arr = resp.json()
        for item in arr:
            if(item['id'] in coins_id):
                if(best_rate[item['id']] > int(item['cmc_coin']['rate_inr'])):
                    pass
                temp = {}
                temp['name'] = item['name']
                temp['rate_inr'] = item['cmc_coin']['rate_inr']

                data.append(temp)

        return json.dumps(data)
    else:
        return None


def send_mail():
    mail()


@app.route('/')
def main():
    return 'Server is running hot!!!'


@app.route('/coinswitch')
def coinswitch():

    return get_latest_data()

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=get_latest_data, trigger="interval", minutes=1)
# scheduler.start()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
