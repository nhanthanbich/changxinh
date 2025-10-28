import streamlit as st
import time
import random

# --- Giả dạng web nghiêm túc, không gây hiểu lầm ---
st.set_page_config(page_title="System Monitor ⚙️", page_icon="🖥️", layout="centered")

# === CSS ===
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === Giao diện ban đầu ===
st.markdown("<h1 class='title'>⚠️ Báo cáo hệ thống bất thường ⚠️</h1>", unsafe_allow_html=True)
st.write("")
time.sleep(1.5)
st.markdown("<p>Phát hiện hoạt động lạ từ thiết bị của bạn...</p>", unsafe_allow_html=True)
time.sleep(2)

# === Nội dung dần chuyển giọng ===
messages = [
    "Hôm nay tớ định khen cậu xinh...",
    "Mà hình như bị bắt bài mất rồi =)))",
    "Đúng là con người tớ cũng thật thà quá.",
    "Nhưng nếu dễ đoán thế thì còn gì vui nữa đúng không :))",
    "Thôi thì để hệ thống tự xử lý vậy.",
    "",
    "Hệ thống xác định: độ sáng tăng bất thường trên màn hình.",
    "Đang phân tích nguyên nhân...",
    "Nguồn gốc ánh sáng: từ nụ cười của Chang.",
    "Kết luận: không phải lỗi hệ thống, mà là do người dùng quá xinh. 💖"
]

placeholder = st.empty()
for msg in messages:
    if msg.strip() == "":
        time.sleep(1.2)  # nghỉ nhịp nhẹ
        continue
    placeholder.markdown(f"<p class='fade-in'>{msg}</p>", unsafe_allow_html=True)
    time.sleep(random.uniform(2.0, 3.0))

st.balloons()
