from binance.client import Client
from pprint import pprint
import time

api_key = '7'
api_secret = ''

client = Client(api_key,api_secret)

# fees = client.get_trade_fee()
# pprint(fees)

# depth = client.get_order_book(symbol='DOGEUSDT')
# pprint(depth)

# trades = client.get_recent_trades(symbol='DOGEUSDT')
# pprint(trades)

# avg_price = client.get_avg_price(symbol='BNBBTC')
# print(avg_price)

while True:
	prices = client.get_all_tickers()
	current_price = ''
	coin_name = 'DOGEUSDT'
	for p in prices:
		if p['symbol'] == coin_name:
			current_price = p
	result = '{} : {}'.format(current_price['symbol'], current_price['price'])
	print(result)
	time.sleep(0.2)
