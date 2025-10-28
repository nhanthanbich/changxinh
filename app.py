import streamlit as st
import time
import random

st.set_page_config(page_title="Chang xinh đẹp 💖", page_icon="💐", layout="centered")

# === CSS style ===
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === Nội dung chính ===
st.markdown("<h1 class='title'>🌸 Lời khen dành riêng cho Chang 🌸</h1>", unsafe_allow_html=True)
st.write("")
messages = [
    "Hôm nay Chang xinh thật đấy.",
    "Không phải do ánh sáng đâu, do Chang đấy.",
    "Càng nhìn càng thấy khó rời mắt.",
    "Nụ cười của Chang đúng kiểu làm người ta nhớ cả ngày.",
    "Nếu có giải thưởng cho vẻ đẹp tự nhiên, chắc Chang lấy cả bảng."
]

placeholder = st.empty()

for msg in messages:
    placeholder.markdown(f"<p class='fade-in'>{msg}</p>", unsafe_allow_html=True)
    time.sleep(2)

st.balloons()
