import streamlit as st
import random
import time

# 게임 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "target_x" not in st.session_state:
    st.session_state.target_x = random.randint(0, 100)
if "target_y" not in st.session_state:
    st.session_state.target_y = random.randint(0, 100)

# 화면을 클릭해서 발사하는 방식
st.title("🎯 간단한 슈팅 게임")
st.write("마우스를 클릭하여 타겟을 맞추세요!")

# 타겟 위치
target_x = st.session_state.target_x
target_y = st.session_state.target_y

# 목표 타겟 표시 (간단한 원)
st.markdown(f'''
    <div style="position: absolute; left: {target_x}%; top: {target_y}%; width: 5vw; height: 5vw; background-color: red; border-radius: 50%;"></div>
''', unsafe_allow_html=True)

# 클릭 좌표 (플레이어가 목표를 향해 총알 발사)
click_x = st.slider("X 좌표 클릭 (0~100)", 0, 100)
click_y = st.slider("Y 좌표 클릭 (0~100)", 0, 100)

# 클릭 시 타겟 맞추기
if st.button("발사!"):
    distance = ((click_x - target_x) ** 2 + (click_y - target_y) ** 2) ** 0.5
    if distance < 10:  # 타겟 범위 안에 들어오면 맞춘 것으로 간주
        st.session_state.score += 1
        st.session_state.target_x = random.randint(0, 100)  # 새 타겟 위치
        st.session_state.target_y = random.randint(0, 100)  # 새 타겟 위치
        st.success(f"타겟을 맞췄습니다! 🎯 점수: {st.session_state.score}")
    else:
        st.warning("타겟을 놓쳤습니다. 다시 시도해보세요!")

# 점수 출력
st.write(f"현재 점수: {st.session_state.score}")

# 게임 종료 조건 (점수 10점 이상)
if st.session_state.score >= 10:
    st.balloons()
    st.success("축하합니다! 10점을 달성했습니다. 게임 종료!")
    if st.button("게임 다시 시작"):
        st.session_state.score = 0
        st.session_state.target_x = random.randint(0, 100)
        st.session_state.target_y = random.randint(0, 100)
