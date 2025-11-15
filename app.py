import streamlit as st
import random
import time

# 게임 설정
st.title("🎯 타겟 맞추기 FPS 게임")
st.write("타겟을 맞추고 점수를 얻어보세요!")

# 게임 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "target" not in st.session_state:
    st.session_state.target = (random.randint(0, 100), random.randint(0, 100))

# 타겟 위치 표시
target_x, target_y = st.session_state.target
st.markdown(
    f'<div style="position: absolute; left: {target_x}%; top: {target_y}%; width: 5vw; height: 5vw; background-color: red; border-radius: 50%;"></div>',
    unsafe_allow_html=True
)

# 점수와 타겟 재설정
click_x = st.slider("X 좌표 클릭 (0~100)", 0, 100)
click_y = st.slider("Y 좌표 클릭 (0~100)", 0, 100)

if st.button("클릭해서 타겟 맞추기"):
    distance = ((click_x - target_x) ** 2 + (click_y - target_y) ** 2) ** 0.5
    if distance < 10:  # 타겟 범위 안이면 맞춘 것으로 간주
        st.session_state.score += 1
        st.session_state.target = (random.randint(0, 100), random.randint(0, 100))  # 새 타겟 위치
        st.success("타겟을 맞췄습니다! 🎯")
    else:
        st.warning("타겟을 놓쳤습니다. 다시 시도해보세요!")

# 점수 출력
st.write(f"현재 점수: {st.session_state.score}")

# 게임 종료 조건 (단순히 10점 이상이면 종료)
if st.session_state.score >= 10:
    st.balloons()
    st.success("축하합니다! 10점을 달성했습니다. 게임 종료!")
    if st.button("게임 다시 시작"):
        st.session_state.score = 0
        st.session_state.target = (random.randint(0, 100), random.randint(0, 100))
