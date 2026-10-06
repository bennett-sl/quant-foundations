# binance aggtrade stream

small python script that prints large usd-m futures prints from binance as they happen. btc, eth, sol, bnb. only shows a trade when the notional is over $15k, so the screen is the big stuff, not every tick.

built this after an older tutorial went quiet. the process stayed up, nothing printed, no error. two separate breaks, both easy to miss.

## what was actually broken

binance moved aggregate trades off the old futures socket. this still connects and then sends nothing:

```text
wss://fstream.binance.com/ws/btcusdt@aggTrade
```

aggtrade is a market stream now. it has to be:

```text
wss://fstream.binance.com/market/ws/btcusdt@aggTrade
```

the other failure was local. python.org python 3.13 on mac does not ship a ca bundle, so the tls handshake died with `certificate verify failed` before any market data. fix is `certifi` passed into the websocket connect, not turning verification off.

pycharm's run window also strips ansi colors. same script, pycharm terminal or mac terminal, colors show up.

## run

```bash
python -m venv .venv
source .venv/bin/activate
pip install certifi pytz termcolor websockets
python binance_aggtrade_stream.py
```

ctrl+c stops it. a keyboardinterrupt traceback after that is just the async loop shutting down.

## why its here

wanted a live market-data feed i could read, and a record of the two fixes. the interesting part was not the print statement. it was a socket that succeeds and stays silent, and an ssl error that looks like the api is down when it is the local trust store.
