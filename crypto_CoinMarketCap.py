import requests
import time

api_key = "" # your api key

token = "" # your token telegram

chat_id = 159509426 # your id telegram

limit = 5900
time_interval = 5

def get_price():

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
    'start':'1',
    'limit':'2',
    
    }

    headers = {

    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key ,
    }

    response = requests.get(url,headers=headers,params=parameters).json()

    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price




def send_update(chat_id,msg):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        price = get_price()
        print(price)

        if price < limit:
            send_update(chat_id,f"lower price: {price}")
        time.sleep(time_interval)
main()

