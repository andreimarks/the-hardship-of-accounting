import random, time
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

def get_unrealized_profit_loss():
    positions = api.list_positions()
    pl = 0
    for position in positions:
        pl += float(position.unrealized_pl)

    return pl

def buy(symbol, qty):
    order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side="buy",
                type="market",
                time_in_force="day"
            )
    
    return order

def buy_with_stop_loss(symbol, qty, stop_loss):
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side="buy",
        type="market",
        time_in_force="day",
        order_class="oto",
        stop_loss={"stop_price":stop_loss}
    )

def buy_with_trail():
    print("Buying with a 25 cent trail.")
    symbol = "GME"
    quote = api.get_last_quote(symbol)
    print(quote.bidprice)

    symbol_bars = api.get_barset(symbol, "minute", 1).df.iloc[0]
    symbol_price  = symbol_bars[symbol]["close"]
    print(symbol_price)

    qty = 1

    buy(symbol, qty)

    #stop_loss = float(quote.bidprice) - .25
    #buy_with_stop_loss(symbol, qty, stop_loss)
    time.sleep(1) # Should hook this into when the order fills.

    trail_price = .25
    sell_with_trailing_stop(symbol, qty, trail_price)

def sell(symbol, qty):
    order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side="sell",
                type="market",
                time_in_force="day"
            )
    
    return order

def sell_with_trailing_stop(symbol, qty, trailing_stop):
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side="sell",
        type="trailing_stop",
        time_in_force="day",
        trail_price=trailing_stop
    )

def sell_all_positions():
    positions = api.list_positions()
    for position in positions:
        sell(position.symbol, position.qty)

def run_daily_random_buy(source_list, purchase_stop_threshold):
    orders = []

    while purchase_stop_threshold > 0:
        print(f"Current purchase limit: {purchase_stop_threshold}")
        ticker = random.choice(source_list)
        pprint(ticker)
        bidprice = 0
        try: 
            quote = api.get_last_trade(ticker)
            pprint(quote.price)

            if quote.price == 0:
                pprint("Nope, price says zero...")
                continue

            bidprice = quote.price
        except:
            bidprice = float(input(f"Get Price for {ticker}:"))

        purchase_stop_threshold -= bidprice
        order = buy(ticker, 1)
        orders.append(order)
        print("----")
    
    return orders

api = tradeapi.REST()

sentimental_holds = ["ATVI", "NFLX", "SPCE", "TTWO", "U"]
sentimental_holds_unavailable = ["NTDOY"]
company_holds = ["CRSP", "NTLA", "BEAM", "FATE"]
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
             "ERTH",
             "LOWC",
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
             "IBB",
             "XBI"]


#start: +$35,545.51

# 03/02/2021
# start: $35,550.03
# end: $35,538.94
"""
while (True):
    buy_with_trail()
    time.sleep(60.0 * 5)

#sell_all_positions()
"""

"""
positions = [asset.symbol for asset in api.list_assets()]
print(positions)

for ticker in watchlist:
    if ticker not in positions:
        print(f"{ticker} is not in positions.")


failed_quotes = []
failed_trades = []
for position in watchlist:
    print(position)
    #print(position.current_price)
    try:
        quote = api.get_last_quote(position)
        #print(quote)
    except:
        failed_quotes.append(position)

    try:
        trade = api.get_last_trade(position)
        #print(trade)
    except:
        failed_trades.append(position)
    print("--------------------------------")
print(failed_quotes)
print(failed_trades)
"""

#limit = 500 #* 1.1 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1
#limit = 500
#orders = run_daily_random_buy(watchlist, limit)
#print(api.get_last_trade("SPYX"))

order = buy("SPYX", 1)
ticker = random.choice(watchlist)
order = buy(ticker, 1)

"""
failed = []
for ticker in watchlist:
    try:
        print(f"{ticker} -- {api.get_last_quote(ticker)}")
    except:
        failed.append(ticker)
        print(f"Failed for {ticker}")

#print(api.get_api_version())
print(failed)
"""