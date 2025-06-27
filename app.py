import streamlit as st
import pandas as pd
from fetch_data import fetch_coin_data
from indicators import calculate_indicators
from ai_module import generate_ai_analysis

st.set_page_config(page_title="Kripto Sinyal Paneli", layout="wide")
st.title("🔮 Kripto Sinyal Paneli (AI Destekli)")

coin = st.selectbox("Coin Seçin", ["pepe", "floki", "dogecoin", "zk-token", "ripple", "dogwifcoin"])
data = fetch_coin_data(coin)

if data is not None:
    indicators = calculate_indicators(data)
    st.subheader("📊 Teknik Göstergeler")
    st.dataframe(indicators.tail(5))

    ai_comment = generate_ai_analysis(indicators)
    st.markdown("### 🤖 AI Yorumu")
    st.info(ai_comment)
else:
    st.error("Veri alınamadı. Lütfen daha sonra tekrar deneyin.")