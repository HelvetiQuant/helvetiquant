
import os
import requests
from flask import jsonify

def get_real_whale_alert():
    api_key = os.getenv("WHALE_ALERT_API_KEY")
    if not api_key:
        return {"error": "API key mancante"}

    url = "https://api.whale-alert.io/v1/transactions"
    params = {
        "api_key": api_key,
        "min_value": 1000000,
        "start": int(__import__("time").time()) - 3600,
        "currency": "usd",
        "limit": 10
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": "Errore API Whale Alert", "status": response.status_code}

    return response.json()
