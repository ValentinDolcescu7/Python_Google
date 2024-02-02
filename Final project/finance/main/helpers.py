import requests
import os
import urllib.parse


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = "pk_bd63c9b54bc04a379c38f0e142e68eee"
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def get_symbols(user):
    symbols = []
    i = 1
    for item in user.portofolio.all():
        symbols.append( (i, item.symbol) )
        i += 1

    return symbols