import requests, json
import random
#import alpaca_trade_api as tradeapi

from config import *
from pprint import pprint

#BASE_URL = "https://paper-api.alpaca.markets"
BASE_URL = "https://api.alpaca.markets"

ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)

#HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-Key": SECRET_KEY}
HEADERS = {"APCA-API-KEY-ID": LIVE_API_KEY, "APCA-API-SECRET-Key": LIVE_SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)

def getting_started_tutorial():
    response = create_order("ICLN", 1, "buy", "market", "gtc")
    #response = create_order("MSFT", 100, "buy", "market", "gtc")
    #orders = get_orders()
    #pprint(orders)
    pass

"""
api = tradeapi.REST(
    base_url=BASE_URL,
    key_id=API_KEY,
    secret_key=SECRET_KEY
)
"""

# Get our account information
#account = api.get_account()

# Check if our account is restricted from trading.
#if account.trading_blocked:
#    print("Account is currently restricted from trading.")

# Check how much money we can use to open new positions.
#print("${} is available as buying power.".format(account.buying_power))

positions = ["PBW"]
ticker = random.choice(positions)
response = create_order(ticker, 2, "buy", "market", "gtc")
pprint(response)
#response = create_order("PBW", 1, "buy", "market", "gtc")
#pprint(response)