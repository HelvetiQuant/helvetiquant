
import requests

BASE_URL = "https://api.bybit.com"

def get_ticker(symbol="1000PEPEUSDT"):
    url = f"{BASE_URL}/v5/market/tickers?category=linear&symbol={symbol}"
    response = requests.get(url)
    data = response.json()

    if data.get("retCode") == 0 and data["result"]["list"]:
        ticker = data["result"]["list"][0]
        return {
            "symbol": ticker["symbol"],
            "price": float(ticker["lastPrice"]),
            "funding_rate": float(ticker["fundingRate"]),
            "open_interest": float(ticker["openInterest"]),
            "volume_24h": float(ticker["turnover24h"]),
        }
    else:
        raise ValueError(f"Errore nel recupero dati Bybit: {data.get('retMsg')}")

# Esempio di test
if __name__ == "__main__":
    print(get_ticker("1000PEPEUSDT"))
