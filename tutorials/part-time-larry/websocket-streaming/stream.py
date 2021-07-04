# https://www.youtube.com/watch?v=fIzm57idu3Y
# installed websocket-client

import websocket, json
from config import *

TICKERS = ["SPCE"]

def on_open(ws):
    print("Opened")

    auth_data = {
        "action": "auth",
        "key": API_KEY,
        "secret": SECRET_KEY
    }

    subscription_data = {
        "action": "subscribe",
        "trades": TICKERS,
        "quotes": TICKERS,
        "bars": TICKERS
    }

    ws.send(json.dumps(auth_data))
    ws.send(json.dumps(subscription_data))

def on_close(ws):
    print("Closed connection.")

def on_message(ws, message):
    print(f'Message: {message}')

def on_error(ws, error):
    print(f'Error: {error}')

socket = "wss://stream.data.alpaca.markets/v2/sip"

# Connect to a socket and define callbacks.
# on_open we authenticate
# on_message we deal with messages coming in.
ws = websocket.WebSocketApp(socket, on_open=on_open, on_close=on_close, on_message=on_message, on_error=on_error)
ws.run_forever()