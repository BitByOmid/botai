from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def analyze_fundamental(crypto_name):
    try:
        coin_data = cg.get_coins_markets(vs_currency='usd', ids=crypto_name.lower())
        return {
            'name': coin_data[0]['name'],
            'category': coin_data[0]['categories'][0],
            'current_price': f"${coin_data[0]['current_price']}"
        }
    except:
        return {
            'name': crypto_name,
            'category': 'Unavailable',
            'current_price': 'Unavailable'
        }