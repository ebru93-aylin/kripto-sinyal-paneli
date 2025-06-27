import ta

def calculate_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['price']).rsi()
    df['macd'] = ta.trend.MACD(df['price']).macd()
    df['bb_bbm'] = ta.volatility.BollingerBands(df['price']).bollinger_mavg()
    df['ao'] = ta.momentum.AwesomeOscillatorIndicator(high=df['price'], low=df['price']).awesome_oscillator()
    return df