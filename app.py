import streamlit as st
import random

st.title("🎮 숫자 맞추기 게임")

# 세션 상태에 랜덤 숫자 저장
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)

guess = st.number_input("1부터 100 사이 숫자를 입력하세요", min_value=1, max_value=100)

if st.button("맞춰보기"):
    if guess == st.session_state.answer:
        st.success("🎉 정답입니다!")
        if st.button("게임 다시 시작"):
            st.session_state.answer = random.randint(1, 100)
    elif guess < st.session_state.answer:
        st.warning("더 큰 숫자입니다!")
    else:
        st.warning("더 작은 숫자입니다!")
