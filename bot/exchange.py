import os
from typing import Dict, Any

from binance.client import Client
from binance.exceptions import BinanceAPIException

def make_client() -> Client:
    key = os.getenv("BINANCE_API_KEY", "")
    secret = os.getenv("BINANCE_API_SECRET", "")
    if not key or not secret:
        raise RuntimeError("Faltan BINANCE_API_KEY / BINANCE_API_SECRET")
    return Client(api_key=key, api_secret=secret)

def get_price(symbol: str) -> float:
    client = make_client()
    try:
        data: Dict[str, Any] = client.get_symbol_ticker(symbol=symbol)
        return float(data["price"])
    except BinanceAPIException as e:
        raise RuntimeError(f"Binance error: {e.message}") from e
