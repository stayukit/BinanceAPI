from tkinter import *
from binance.client import Client
from pprint import pprint
import time

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

try:
	print(doge['asset'])
except TypeError:
	textdoge = 'DOGE : None'
else:
	textdoge = '{} : {} (In order: {})'.format(doge['asset'], doge['free'], doge['locked'])

try:
	print(usdt['asset'])
except TypeError:
	textusdt = 'USDT : None'
else:
	textusdt = '{} : {} (In order: {})'.format(usdt['asset'], usdt['free'], usdt['locked'])

alltext = textdoge + '\n' + textusdt


def UpdatePrice():
	prices = client.get_all_tickers()
	current_price = ''
	coin_name = 'DOGEUSDT'
	for p in prices:
		if p['symbol'] == coin_name:
			current_price = p
	# print('+++++++')
	# print(current_price)
	time.sleep(0.2)
	# {'symbol': 'DOGEUSDT', 'price': '0.05278730'}
	v_current.set('{} : {}'.format(current_price['symbol'],current_price['price']))
	R1.after(100,UpdatePrice)

################################
GUI = Tk()
GUI.geometry('500x300')
GUI.title('Crypto')

Font1 = ('Angsana New', 32)
Font2 = ('Angsana New', 20)
Font3 = ('Impact', 20)
L1 = Label(GUI, text = 'Balance', font=Font1)
L1.pack()

v_balance = StringVar()
v_balance.set(alltext)
BL = Label(GUI, textvariable=v_balance, font=Font2, fg = 'green' )
BL.pack()

# L2 = Label(GUI, text = 'Current Price', font=Font1)
# L2.pack()

v_current = StringVar()
R1 = Label(GUI, textvariable=v_current, font=Font3)
R1.pack()


UpdatePrice()
GUI.mainloop()
