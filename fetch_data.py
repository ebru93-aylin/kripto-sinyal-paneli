def fetch_coin_data(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {"vs_currency": "usd", "days": "7", "interval": "daily"}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"API hatası: {response.status_code}")
            return None
        data = response.json()
        prices = data["prices"]
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        return df
    except Exception as e:
        print(f"Hata: {e}")
        return None
