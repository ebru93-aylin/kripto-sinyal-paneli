def generate_ai_analysis(df):
    latest = df.iloc[-1]
    if latest['rsi'] < 30:
        return "RSI çok düşük, olası dip fırsatı."
    elif latest['rsi'] > 70:
        return "RSI çok yüksek, olası zirve dikkat!"
    else:
        return "RSI nötr, trend takip edilmeli."