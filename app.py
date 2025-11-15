import streamlit as st
import random

st.title("🎰 슬롯머신 게임 (포인트 버전)")
st.write("버튼을 눌러 슬롯을 돌려보세요! 💰")

# 세션 상태 초기화
if "points" not in st.session_state:
    st.session_state.points = 100  # 시작 포인트

# 슬롯 심볼
symbols = ["🍒", "🍋", "🍇", "⭐", "💎"]

# 베팅 금액 설정
bet = st.slider("베팅 포인트", 10, 50, 10)

# 슬롯 돌리기
if st.button("🎲 슬롯 돌리기"):
    if st.session_state.points < bet:
        st.error("포인트가 부족합니다! 게임 종료 😢")
    else:
        st.session_state.points -= bet
        result = [random.choice(symbols) for _ in range(3)]
        st.write(" | ".join(result))

        # 결과 계산
        if len(set(result)) == 1:  # 3개 일치
            win = bet * 5
            st.session_state.points += win
            st.success(f"🎉 잭팟! {win} 포인트 획득!")
        elif len(set(result)) == 2:  # 2개 일치
            win = bet * 2
            st.session_state.points += win
            st.info(f"👍 2개 일치! {win} 포인트 획득!")
        else:
            st.warning("💨 아쉽지만 꽝!")

st.write(f"💰 현재 포인트: **{st.session_state.points}**")

# 리셋 버튼
if st.button("🔄 포인트 초기화"):
    st.session_state.points = 100
    st.info("포인트가 100으로 초기화되었습니다.")
