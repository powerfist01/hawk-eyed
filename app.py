from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from services.mailer.mailer import mail

import requests, json

app = Flask(__name__)

coins_id = [1, 6, 210]

def get_latest_data():

    resp = requests.get('https://coinswitch.co/proxy/in/api/v1/coins')
    if(resp.status_code == 200):
        data = []
        arr = resp.json()
        for item in arr:
            if(item['id'] in coins_id):
                temp = {}
                temp['name'] = item['name']
                temp['rate_inr'] = item['cmc_coin']['rate_inr']
                
                data.append(temp)

        return json.dumps(data)
    else:
        return None

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