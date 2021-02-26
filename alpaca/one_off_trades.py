import random
import alpaca_trade_api as tradeapi

def swap_spy_for_spyx(api):
    """2021/02/24
    
    One off function written when I wanted to buy a roughly equivalent 
    amount of SPYX shares (i.e. Fossil Fuel Free) for my SPY shares.
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