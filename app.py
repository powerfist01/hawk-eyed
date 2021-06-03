from flask import Flask, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from services.mailer.mailer import Mail

import requests, json

app = Flask(__name__)

coins_name = ['Bitcoin','Ethereum','Polygon','Cardano', 'QuarkChain', 'VeChain','iExec RLC']

coins = [
    {"id": 210, "name": "Cardano", "rate": 140}, 
    {"id": 1, "name": "Bitcoin", "rate": 2900000}, 
    {"id": 6, "name": "Ethereum", "rate": 200000}, 
    {"id": 276, "name": "Polygon", "rate": 150}, 
    {"id": 205, "name": "Maker", "rate": 270000}
]

coins_best_rate = {
    'Bitcoin': 2900000,
    'Ethereum': 200000,
    'Maker': 270000,
    'Cardano': 140,
    'Polygon': 150
}

def get_latest_data():

    resp = requests.get('https://coinswitch.co/proxy/in/api/v1/coins')
    if(resp.status_code == 200):
        data = []
        arr = resp.json()
        for item in arr:
            if(item['name'] in coins_name):
                temp = {}
                temp['name'] = item['name']
                temp['rate_inr'] = item['cmc_coin']['rate_inr']

                data.append(temp)

        return data
    else:
        return None


def send_mail():
    mail = Mail()
    mail.send_mail(data='not-yet')

@app.route('/')
def main():
    return 'Server is running hot!!!'


@app.route('/coinswitch')
def coinswitch():

    coins = get_latest_data()
    return render_template('index.html', coins = coins)

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=get_latest_data, trigger="interval", minutes=1)
# scheduler.start()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
