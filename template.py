from binance.client import Client
from pprint import pprint

api_key = '7'
api_secret = ''

client = Client(api_key,api_secret)

# Account endpoint / Account info
info = client.get_account()
# pprint(info)

doge = client.get_asset_balance(asset='DOGE')
usdt = client.get_asset_balance(asset='USDT')
print('DOGE', doge)
print('USDT', usdt)
