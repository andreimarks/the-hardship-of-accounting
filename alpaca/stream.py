import logging

from alpaca_trade_api.stream import Stream

log = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.DEBUG)
    feed = "sip"
    stream = Stream(data_feed=feed, raw_data=True)	
    print(stream)
    #stream.subscribe_trade_updates(print_trade_update)


if __name__ == "__main__":
    main()	