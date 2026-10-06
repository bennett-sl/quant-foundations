"""
binance futures aggregate trade stream, with the two fixes i needed
after copying an older tutorial that used to work.

the old code looked like this:

    wss://fstream.binance.com/ws/btcusdt@aggTrade
    async with connect(uri) as websocket:

that used to dump trades right away. now it just sits there. two things broke.

1. binance moved the agg trade stream. it has to go through /market now.
   the old /ws/ url still connects, then sends nothing, and it doesnt even error.
   the one that works is wss://fstream.binance.com/market/ws/<symbol>@aggTrade

2. python from python.org on mac doesnt trust certificates out of the box.
   you get ssl.SSLCertVerificationError: certificate verify failed.
   certifi is just a list of real certificate authorities. pass it into connect().

pycharms run window isnt a real terminal, so the colors from cprint get stripped.
run it in pycharms terminal tab, or in the mac terminal with the project venv, if you want the colors:

    /path/to/project/.venv/bin/python this_file.py

ctrl+c stops it. the keyboardinterrupt / cancellederror dump after that is normal, it already quit.
"""

import asyncio
import json
import ssl
from datetime import datetime

import certifi
import pytz
from termcolor import cprint
from websockets import connect

SYMBOLS = ["btcusdt", "ethusdt", "solusdt", "bnbusdt"]
STREAM_URL = "wss://fstream.binance.com/market/ws/{symbol}@aggTrade"
MIN_USD = 15_000

SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())


def describe(symbol, price, quantity, trade_time_ms, is_buyer_maker):
    usd_size = price * quantity
    if usd_size < MIN_USD:
        return None

    side = "SELL" if is_buyer_maker else "BUY"
    color = "red" if side == "SELL" else "green"
    stars = ""
    if usd_size >= 500_000:
        stars = "**"
        color = "magenta" if side == "SELL" else "blue"
    elif usd_size >= 100_000:
        stars = "*"

    clock = datetime.fromtimestamp(
        trade_time_ms / 1000, pytz.timezone("US/Eastern")
    ).strftime("%H:%M:%S")
    name = symbol.upper().removesuffix("USDT")
    return f"{stars} {side} {name} {clock} ${usd_size:,.0f}", color


async def stream(symbol):
    uri = STREAM_URL.format(symbol=symbol)
    async with connect(uri, ssl=SSL_CONTEXT) as websocket:
        async for message in websocket:
            data = json.loads(message)
            shown = describe(
                symbol,
                float(data["p"]),
                float(data["q"]),
                int(data["T"]),
                data["m"],
            )
            if shown:
                text, color = shown
                cprint(text, "white", f"on_{color}", attrs=["bold"])


async def main():
    await asyncio.gather(*(stream(symbol) for symbol in SYMBOLS))


if __name__ == "__main__":
    asyncio.run(main())
