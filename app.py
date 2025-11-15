import streamlit as st
import random
import time

# 게임 설정
st.title("🕹️ 간단한 점프맵 게임")
st.write("스페이스바를 눌러 점프하세요!")

# 게임 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "jump_height" not in st.session_state:
    st.session_state.jump_height = 0

# 점프 높이 슬라이더
jump = st.slider("점프 높이 조정", min_value=1, max_value=100, value=50)

# 점프 버튼 (간단한 버튼으로 점프 효과 시뮬레이션)
if st.button("점프!"):
    st.session_state.jump_height = jump
    st.session_state.score += 1

# 화면 표시 (게임을 위한 간단한 UI)
st.write(f"현재 점프 높이: {st.session_state.jump_height}단위")
st.write(f"현재 점수: {st.session_state.score}")

# 플랫폼 표시 (랜덤하게 위치 변경)
platforms = [random.randint(20, 80) for _ in range(5)]
st.write("플랫폼 위치: ", platforms)

# 게임 종료 조건
if st.session_state.jump_height > max(platforms):  # 점프 높이가 모든 플랫폼을 넘으면 게임 오버
    st.balloons()
    st.success("게임 종료! 점프 성공!")
    if st.button("게임 다시 시작"):
        st.session_state.score = 0
        st.session_state.jump_height = 0
else:
    st.warning("플랫폼을 피하며 점프하세요!")
