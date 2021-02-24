import random
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

sentimental_holds = ["U"]
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
             "THCX"]

orders = run_daily_random_buy(watchlist, 500)