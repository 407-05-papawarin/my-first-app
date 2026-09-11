import time
import streamlit as st

st.title("⏱️ เกมทายชื่อแอปพลิเคชั่นจับเวลา (ภาษาอังกฤษ)")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    if u_ans1 == "Line":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    if u_ans2 == "Netflix":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    if u_ans3 == "Roblox":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "X":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    if u_ans5 == "Instagram":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} / 5 คะแนน")

    if score == 5:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.is_ended:
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: แอปแชทสีเขียวที่คนไทยใช้ส่งสติ๊กเกอร์สวัสดีวันจันทร์มากที่สุด 💚",
    key="ans1_val"
)

ans2 = st.text_input(
    "ข้อ 2: แอปสีแดงดำ เอาไว้ดูหนังดูซีรีย์ ลงท้ายด้วยตัว X 🎥",
    key="ans2_val"
)

ans3 = st.text_input(
    "ข้อ 3: แอปที่เด็ก Gen Alpha ชอบเล่น มีเงินในเกมเรียกว่า Robux 💸",
    key="ans3_val"
)

ans4 = st.text_input(
    "ข้อ 4: แอปปกสีดำ ที่เอาไว้พูดคุยเกี่ยวกับประเด็นร้อนทางสังคม มีชื่อเดิมว่าทวิตเตอร์ 📱",
    key="ans4_val"
)

ans5 = st.text_input(
    "ข้อ 5: แอปที่ Gen Z ชอบใช้ เอาไว้ลงสตอรี่ ลงรูป และพูดคุยกัน มีสีรุ้ง 🌈",
    key="ans5_val"
)

if "start" in st.session_state and not st.session_state.is_ended:
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

if st.session_state.is_ended:
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val,
        st.session_state.ans5_val
    )

st.divider()

