import requests

class Coinswitch:
    top_coins = ['Bitcoin', 'Ethereum', 'Cardano', 'Solana', 'Polygon']

    def get_latest_data(self, coin=''):

        try:
            resp = requests.get('https://coinswitch.co/proxy/in/api/v1/coins')
            arr = resp.json()
            if(coin):
                for item in arr:
                    if(item['name'] == coin):
                        return item
                return {'details':'Coin not found!'}
            else:
                data = []
                for item in arr:
                    if(item['name'] in self.top_coins):
                        temp = {}
                        temp['name'] = item['name']
                        temp['rate_inr'] = item['cmc_coin']['rate_inr']

                        data.append(temp)

                return data
        except Exception as e:
            return {'details': 'API not working, sorry :('}