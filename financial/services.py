import requests

def get_stock_price(symbol):
    url = f'https://api.iextrading.com/1.0/stock/{symbol}/batch?types=quote'
    r = requests.get(url)
    jsonResponse = r.json()
    return jsonResponse['quote']['latestPrice']