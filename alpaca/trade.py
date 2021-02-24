import math, random
import alpaca_trade_api as tradeapi

from pprint import pprint

def get_account_info():
    # Get our account information
    account = api.get_account()
    print(account)

    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print("Account is currently restricted from trading.")

    # Check how much cash is in the account.
    print("${} is available as cash.".format(account.cash))

    # Check how much money we can use to open new positions.
    print("${} is available as buying power.".format(account.buying_power))


def buy(symbol, qty):
    order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side="buy",
                type="market",
                time_in_force="day"
            )
    
    return order

def sell(symbol, qty):
    order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side="sell",
                type="market",
                time_in_force="day"
            )
    
    return order

def run_daily_random_buy(source_list, purchase_stop_threshold):
    orders = []

    while purchase_stop_threshold > 0:
        print(f"Current purchase limit: {purchase_stop_threshold}")
        ticker = random.choice(source_list)
        pprint(ticker)
        quote = api.get_last_quote(ticker)
        pprint(quote.bidprice)
        purchase_stop_threshold -= quote.bidprice
        order = buy(ticker, 1)
        orders.append(order)
        print("----")
    
    return orders


api = tradeapi.REST()

sentimental_holds = ["ATVI", "U"]
watchlist = ["TAN",
             "QCLN",
             "PBW",
             "ICLN",
             "FAN",
             "BOTZ",
             "ARKG",
             "ACES",
             "ARKK",
             "ARKQ",
             "ROBO",
             "PHO",
             "UFO",
             "PZD",
             "LOWC",
             "SPCE",
             "AAPL",
             "MSFT",
             "SPYX",
             "GRID",
             "YOLO",
             "CNBS",
             "THCX",
             #"DIET",
             #"QTUM",
             #"ORG",
             "NTDOY"]

orders = run_daily_random_buy(watchlist, 500)

"""
# Get current shares of SPY
positions = api.list_positions()
spy_count = 0
for position in positions:
    if position.symbol == "SPY":
        spy_count = int(position.qty)

print(f"{spy_count} shares of SPY")

# Get quotes
spy_price = api.get_last_quote("SPY").bidprice
spyx_price = api.get_last_quote("SPYX").bidprice
print(f"SPY: {spy_price}")
print(f"SPYX: {spyx_price}")
print("----")

# Plan orders
spyx_count = math.ceil(spy_price/spyx_price) * spy_count
print(f"Sell {spy_count} shares of SPYX")
print(f"Buy {spyx_count} shares of SPYX")

sell_order = sell("SPY", spy_count)
pprint(sell_order)

buy_order = buy("SPYX", spyx_count)
pprint(buy_order)
"""
